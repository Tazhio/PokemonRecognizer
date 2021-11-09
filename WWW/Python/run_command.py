import subprocess
from subprocess import PIPE, run
import json
import pypokedex


def get_token():
    token_command='curl https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens -X POST -i -d @data.json --header "Content-Type: application/json"'
    token_all = run(token_command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    token_all = token_all.stdout
    start_str='X-Subject-Token: '
    end_str='X-Request-Id'
   
    start_pos= token_all.index(start_str)
    end_pos = token_all.index(end_str)
    token_result=token_all[start_pos+17:end_pos-1]
    return token_result

def get_pokemon_ID(image_path):
    token=get_token()
    c1 = "curl -F 'images=@"
    # image_path = "pikachu.jpg"
    c1_end = "'"
    c2 = " -H 'X-Auth-Token:"
    c2_end = "'"
    c3 = " -X POST "
    ai_url ='https://6ac81cdfac4f4a30be9591fc2f2bb682.apig.cn-north-4.huaweicloudapis.com/v1/infers/98363f0a-d77d-4c45-9223-ea0ecd0bcaaf'
    command_f = c1 + image_path + c1_end + c2 + token + c2_end + c3 + ai_url
    result = run(command_f, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    predict_result = result.stdout
    # example_working_output = '{"predicted_label": "Pikachu", "scores": [["Pikachu", "0.986"], ["Raichu", "0.007"], ["Weedle", "0.002"], ["Abra", "0.000"], ["Aerodactyl", "0.000"]]}'

    result_dict = u'' + predict_result
    print(predict_result)
    result_dict = json.loads(result_dict)
    try:
        pokemon_name = result_dict['predicted_label']
    except KeyError:
        return -1

    #
    # print(result_dict['predicted_label'])

    pokemon_itself = pypokedex.get(name=pokemon_name)
    pokemon_id = pokemon_itself.dex
    # print(pokemon_id)

    return pokemon_id

if __name__=='__main__':
    image_path = "pikachu.jpg"
    print(get_pokemon_ID('squirtle.png'))

