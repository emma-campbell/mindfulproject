FROM node:lts-alpine

WORKDIR /client

ENV PATH /client/node_modules/.bin:$PATH
COPY . .
RUN yarn
CMD ["yarn", "serve"]