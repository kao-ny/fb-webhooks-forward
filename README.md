# fb-webhooks-forward

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nyan-salmon/fb-webhooks-forward)

## なにこれ
某コミュニケーションツール開発中に、FacebookのWebhooksを受け取って色々したかった。

FacebookのWebhooksを受け取るにはhttpsが必須だったが、テスト用環境はhttpで受け取れないため、heroku(https) -> テスト環境(http)と転送するもの

（あまりよくないとは思いつつも、期日的に...）

## What is this
To receive facebook webhooks, required to use https connection.

But my testing environment can only http connection.

Deploy this tool to heroku, and transfer webhooks from heroku(https) to the test environment(http).

## License
This software is released under the MIT License, see LICENSE.
