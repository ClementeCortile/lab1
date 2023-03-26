import os
import requests
import replicate


zip_path = "goku.zip"
zip_filename = zip_path.split("/")[-1]


def main():
    # Upload inputs to cloud storage.
    # You can skip this step if your zip file is already on the internet and accessible over HTTP
    upload_response = requests.post(
        "https://dreambooth-api-experimental.replicate.com/v1/upload/" + zip_filename,
        headers={
            "Authorization": "Token " + os.environ["REPLICATE_API_TOKEN"]},
    ).json()

    with open(zip_path,
              "rb") as f:
        requests.put(upload_response["upload_url"],
                     data=f)
    zip_url = upload_response["serving_url"]

    # Train the model
    lora_url = replicate.run(
        "replicate/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",
        input={"instance_data": zip_url, "task": "style"}
    )
    print(1)

if __name__ == "__main__":
    main()
