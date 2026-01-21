import pathlib
import pooch


TEST_DATA_ARCHIVE = "https://github.com/3dgeo-heidelberg/py4dgeo-test-data/releases/download/2024-06-28/data.tar.gz"
TEST_DATA_CHECKSUM = "5ee51a43b008181b829113d8b967cdf519eae4ac37a3301f1eaf53d15d3016cc"


for entry in pathlib.Path(pooch.os_cache("foo")).iterdir():
    print(entry)


print(pooch.retrieve(
            TEST_DATA_ARCHIVE,
            TEST_DATA_CHECKSUM,
            path=pooch.os_cache("foo"),
            downloader=pooch.HTTPDownloader(timeout=(3, None)),
            processor=pooch.Untar(extract_dir="."),
        ))