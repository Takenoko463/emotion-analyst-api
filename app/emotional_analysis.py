emotions = ["aware","shame","anger","unpleasant","fear","surprise","love","excitement","relax","pleasant"]
def get_emotional_words():
    emotional_words = {}
    for emotion in emotions:
        emotional_words[emotion] = []
        with open("./app/emotions/" + emotion + "_uncoded.txt", "r") as f:
            for line in f:
                line = line.replace('\n', '')
                emotional_words[emotion].append(line)
    return emotional_words


def count_emotional_words(sentences, emotional_words):
    count_emotions = [0] * len(emotional_words.keys())
    for idx, emotion in enumerate(emotional_words.keys()):
        for word in emotional_words[emotion]:
            count_emotions[idx] += sentences.count(word)
    return count_emotions


def get_analysis_word(word):
    emotional_words = get_emotional_words()
    count_emotions = count_emotional_words(word, emotional_words)
    
    emotion_models=[{emotion:count_emotion} for emotion, count_emotion in zip(emotions, count_emotions)]
    return dict(word=word,emotions=emotion_models)

def get_analysis_words(words):
    return [get_analysis_word(word) for word in words]

if __name__=="__main__":
    print(get_analysis_word("嬉しい"))
    
    print(
        get_analysis_words(["嬉しい","悲しい"])
    )
