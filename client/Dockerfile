FROM node:lts-alpine

RUN apk update && \
    apk add --progress git

RUN npm install -g @vue/cli
WORKDIR /client

ENV PATH /client/node_modules/.bin:$PATH
COPY package.json .
RUN yarn

COPY . . 
CMD ["yarn", "serve"]