import os
import hydra
import pandas as pd
from omegaconf import DictConfig

from src.utils import getLogger, createDirectory
from src.imgCrawler import crawlTagImg


@hydra.main(version_base="1.2", config_path="configs", config_name="imgs.yaml")
def main(config: DictConfig = None) -> None:
    # set logger
    log = getLogger()
    log.propagate = False

    # check dir
    createDirectory(os.path.join(config.out_dir))

    log.info("Start %s Img crawling with query %s ...", config.origin_Tag, config.query_Tag)
    Img_infos, failed_crawling = crawlTagImg(config.origin_Tag, config.query_Tag, config.collection_url, config.n_scroll, log)

    log.info("%d img crawled", len(Img_infos))
    log.info("Num of failed crawling: %d", failed_crawling)

    # save crwaling results
    csv_path = os.path.join(config.out_dir, f"{config.origin_Tag}_{config.query_Tag}_{config.keys_filename}")
    log.info("Save concatencated Img_infos to %s", csv_path)
    Img_infos_df = pd.DataFrame(Img_infos)
    Img_infos_df.to_csv(csv_path, index=False)


if __name__ == "__main__":
    main()
