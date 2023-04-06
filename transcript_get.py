from youtube_transcript_api import YouTubeTranscriptApi

# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('_v_fgW2SkkQ&ab_channel=DataIndependent')
transcript = []
# iterate over all available transcripts
for a in transcript_list:

    # the Transcript object provides metadata properties

    #transcript = transcript_list.find_transcript([ 'en'])
    # fetch the actual transcript data

    x = a.fetch()
    #print(x)
    transcript.append(x)
transcript = transcript[0]

new_transcript = []
for i in range(len(transcript)):
    new_transcript.append(transcript[i]["text"])

A = "\n".join(new_transcript)

print(A)














    #print(transcript)

    #xoxb-1211064436931-5033105842086-DnwboifcZxp09jndsDiFdbvl
    #2
    #xapp-1-A051J9KA4SV-5042212527588-0b9babb6a6987e35730a78636eaadf39af77096717c0efbf06df3ca341415597
    #chatgpt
    #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

    #os.environ["OPENAI_API_KEY"] = "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"