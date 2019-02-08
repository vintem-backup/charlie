# Charlie tradebot: About elasticsearch database

## Create........: 2019-FEV-07
## Last Update...: 2019-FEV-07
#### Author: Marcus Mello (mandealista@gmail.com)

[PT_br]

## Estrutura url:

host:porta/index/type/id --> data{"key":"value"}

### Modelo

1 - Dados de mercado
localhost:9200/marketdata/btcusdt/binance/<timestamp> --> {"Open":"3839.94", "High":"3839.98", "Low":"3735.0", "Close":"3735.0", "Volume":"24.85793", "N_of_trades":"129.0"}

2 - Logs operacionais
