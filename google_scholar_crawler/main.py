import time
import sys
import json
import os
from datetime import datetime
from scholarly import scholarly, ProxyGenerator


def setup_proxy():
    """Set up scholarly proxy via FreeProxy, with fallback to direct connection."""
    try:
        pg = ProxyGenerator()
        success = pg.FreeProxies()
        if success:
            scholarly.use_proxy(pg)
            print("[INFO] Proxy configured via FreeProxies")
            return
    except Exception as e:
        print(f"[WARN] FreeProxies failed: {e}")

    # Fallback: direct connection without proxy (retry logic in main() still applies)
    print("[INFO] Falling back to direct connection (no proxy)")
    try:
        scholarly.use_proxy(None)
    except Exception:
        pass


def retry_fill(author, sections, max_retries=3):
    """Retry scholarly.fill() with exponential backoff."""
    for attempt in range(1, max_retries + 1):
        try:
            author = scholarly.fill(author, sections=sections)
            return author
        except Exception as e:
            wait = 10 * attempt
            print(f"[WARN] fill() attempt {attempt}/{max_retries} failed: {e}. Retrying in {wait}s...")
            if attempt == max_retries:
                raise
            time.sleep(wait)
    return author


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "")
    if not scholar_id:
        print("[ERROR] GOOGLE_SCHOLAR_ID environment variable not set")
        sys.exit(1)

    # Step 1: Configure proxy
    setup_proxy()

    # Step 2: Search author with retry
    author = None
    for attempt in range(1, 4):
        try:
            author = scholarly.search_author_id(scholar_id)
            print(f"[INFO] Author found: {author.get('name', 'unknown')}")
            break
        except Exception as e:
            wait = 10 * attempt
            print(f"[WARN] search_author_id() attempt {attempt}/3 failed: {e}. Retrying in {wait}s...")
            if attempt == 3:
                print("[ERROR] Failed to search author after 3 attempts")
                sys.exit(1)
            time.sleep(wait)

    # Step 3: Fill author profile with retry
    author = retry_fill(
        author,
        sections=["basics", "indices", "counts", "publications"],
        max_retries=3,
    )

    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}
    print(json.dumps(author, indent=2))

    # Step 4: Write output files
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as f:
        json.dump(author, f, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
        json.dump(shieldio_data, f, ensure_ascii=False)

    print(f"[INFO] Done. Citations: {author['citedby']}")


if __name__ == "__main__":
    main()
