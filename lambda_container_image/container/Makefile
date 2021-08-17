FUNC_NAME   := sandbox_container_lambda
IMG_NAME    := sandbox_container_lambda_image
IMG_TAG     := ${IMG_NAME}:latest
REMOTE_REPO := ${AWS_ID}.dkr.ecr.ap-northeast-1.amazonaws.com


login:
	@$$(aws ecr get-login --no-include-email --region ap-northeast-1 --profile ${PROFILE})

build:
	@docker build -t ${IMG_TAG} .

deploy: build login
	@docker tag ${IMG_TAG} ${REMOTE_REPO}/${IMG_TAG}
	@docker push ${REMOTE_REPO}/${IMG_TAG}
	@aws lambda update-function-code --function-name ${FUNC_NAME} --image-uri ${REMOTE_REPO}/${IMG_TAG} --publish --profile ${PROFILE}
	@aws lambda wait function-updated --function-name ${FUNC_NAME} --profile ${PROFILE}

local_test:
	@docker run -it --rm --entrypoint=/bin/bash ${IMG_TAG}