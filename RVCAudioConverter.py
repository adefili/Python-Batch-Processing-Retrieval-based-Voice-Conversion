from utils import download_models, download_spongebob_custom_model, create_dot_env_file
from pathlib import Path
from rvc.modules.vc.modules import VC
import soundfile as sf
import os

class RVCAudioConverter:
    def __init__(self, model_pth_path, model_index_path, skip_first_setup=False, skip_spongebob_model=False):
        if not skip_first_setup:
            create_dot_env_file()
            download_models()
        if not skip_spongebob_model:
            download_spongebob_custom_model()
        self.vc = VC()
        self.model_pth_path = model_pth_path
        self.model_index_path = model_index_path
        self.vc.get_vc(self.model_pth_path)

    def set_model(self, model_pth_path, model_index_path):
        self.model_pth_path = model_pth_path
        self.model_index_path = model_index_path
        self.vc.get_vc(self.model_pth_path)

    def create_empty_dir_if_not_exist(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def parse_single_audio(self, input_audio_path, output_audio_path, output_format="wav"):
        print("parsing: " + input_audio_path + " -> " + output_audio_path)

        data, samplerate = sf.read(input_audio_path)
        tmp_input_wav_audio_path = "tmp/tmp_input_converted_audio.wav"
        self.create_empty_dir_if_not_exist("tmp")
        sf.write(tmp_input_wav_audio_path, data, samplerate)

        tgt_sr, audio_opt, times, _ = self.vc.vc_inference(1, Path(tmp_input_wav_audio_path), index_file=self.model_index_path)

        parsed_base_path = output_audio_path.split("/")[0]
        parsed_filename = output_audio_path.split("/")[1].split(".")[0]
        parsed_path = parsed_base_path+"/"+parsed_filename+"."+output_format

        sf.write(parsed_path, audio_opt, tgt_sr)
        os.remove(tmp_input_wav_audio_path)

    def parse_batch_audio(self, input_audio_folder_path, output_audio_folder_path, output_format="wav"):
        self.create_empty_dir_if_not_exist(output_audio_folder_path)
        for filename in os.listdir(input_audio_folder_path):
            input_file_path = os.path.join(input_audio_folder_path, filename)
            output_file_path = os.path.join(output_audio_folder_path, filename)
            self.parse_single_audio(input_file_path, output_file_path, output_format=output_format)
        
