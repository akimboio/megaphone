from django.http import HttpResponse
import subprocess
import os
import uuid


def tts(request, format="mp4f"):

    voice = request.REQUEST.get("voice", "Kathy")
    format = str(format).lower()

    format_conversions = {
        "aaif": ("aaif", "aiff", "audio/aiff"),
        "wave": ("WAVE", "wav", "audio/wave"),
        "mp4f": ("mp4f", "mp4", "audio/mp4a-latm")
        }

    # Grab the string that we wish to encode to audio
    encode_string = request.REQUEST["string"] 

    # Create a temporary file name for the audio file
    tmp_file = "/tmp/{0}.{1}".format(str(uuid.uuid4()), format_conversions[format][1])

    cmd = "say -o {0} --file-format={1} -v {2}".format(
        tmp_file,
        format_conversions[format][0],
        voice
        )

    # Create a temporary audio file of the string
    p = subprocess.Popen(cmd,
                     shell=True,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE
                     )
    
    (stdout, stderr) = p.communicate(encode_string.replace('"', ''))

    # Read the audio file into memory
    audio_buffer = open(tmp_file).read()

    # Remove the tmp file
    os.remove(tmp_file)

    # Return the contents of the audio file via HTTP
    response = HttpResponse(audio_buffer, mimetype=format_conversions[format][2])
    response['Content-Disposition'] = "filename={0}.{1}".format("tts-audio", format_conversions[format][1])
    return response
