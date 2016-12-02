build:
	docker build -t rekognition  .

run: build
	docker run -ti --rm -v `pwd`/outcomes:/root/outcomes rekognition
