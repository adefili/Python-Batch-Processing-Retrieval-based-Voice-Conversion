use Retrieval-based-Voice-Conversion with python code to ..., permtis easy batch processing, easy models download, convert audio from/to wav

## Requirements
working with `python 3.10.14`

## Installation
clone the repositories

create a python env

ensure `pip 24.0` is installed. pip 25.x or higher will break

pip install -r requirements.txt

install required packages using "pip install git+https://github.com/RVC-Project/Retrieval-based-Voice-Conversion.git@develop"

rvc folder is alredy attached in the repositories. alternatively you get it from "https://github.com/RVC-Project/Retrieval-based-Voice-Conversion/tree/develop/rvc"

to permit unsafe pickles loading and avoid errors, i had to do the following changes inside `rvc/modules/vc/modules.py`(the one in the repository is alredy changed) and `{your python env or python installation path}/Lib/site-packages/fairseq/checkpoint_utils.py`

from torch.load(...) -> torch.load(..., weights_only=False)

# Running
the scripts manage to download all needed models + a custom spongebob model to do a quick "hello world"


