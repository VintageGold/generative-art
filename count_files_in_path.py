import tarfile
import Path

def count_file_contents():
    tar = tarfile.open(Path('data/punks-sample.tgz'), "r:gz")
    return len(tar.getnames())