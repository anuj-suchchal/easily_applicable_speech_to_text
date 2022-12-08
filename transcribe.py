import torch
import nemo.collections.asr as nemo_asr

example_file = "20200918164725_61304_4.wav"

if torch.cuda.is_available():
    device = torch.device(f'cuda:0')

asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_en_quartznet15x5")
result = asr_model.transcribe(paths2audio_files=[example_file])
print(result)
