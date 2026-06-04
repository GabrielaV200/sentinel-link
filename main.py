from src.utils.logger import get_logger

logger = get_logger(__name__)


def main() -> bool:
    logger.info("Sentinel-Link pipeline starting")
    logger.debug("Running ingestion step (stub)")
    logger.info("Sentinel-Link pipeline finished")
    return True


if __name__ == "__main__":
    main()
