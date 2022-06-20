from src import config
from src.utils.util import get_recomendation
import collections
result_dict = {}

for model_result in config.RESULT.glob("*.txt"):
    result = get_recomendation(model_result)
    model_name = model_result.stem
    # print(f"{model_name}:{len(result)}")
    if model_name not in ["MostPop", "SoRec"]:
        result_dict.setdefault(model_name, result)

with open(config.RESULT / "Ensemble.txt", "w") as f:
    for user_id in range(1892):
        final_recommendation = []
        for idx in range(15):
            ensemble_list = []
            for model_name in result_dict.keys():
                try:
                    ensemble_list.append(result_dict[model_name][user_id][idx])
                except IndexError:
                    pass
            counter = collections.Counter(ensemble_list)
            most_vote = counter.most_common(1)[0][0]
            final_recommendation.append(str(most_vote))
        text = " ".join(final_recommendation)
        text +='\n'
        f.write(text)
        
# print(counter.most_common(1)[0][0])
#[6373, 89, 89, 89, 101, 329]
#[8388, 89, 89, 89, 72, 72]