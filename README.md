# Scryp
Scryp is a lightweight REST API which implement the main features of [Moneywagon](https://github.com/priestc/moneywagon).

#### Why *Scryp*?
According to [Cambridge Dictionary](https://dictionary.cambridge.org/dictionary/english/scrip):
> Scrip is "something that is not currency but that can be used in the same way as money." 

So, Scrip + Cryptocurrency = **Scryp**: because crypto coins aren't just an ordinary currency, they're better!

## Usage
You can test the API with the [demo server](https://scryp.herokuapp.com), but I *strongly recommend* deploying on your own server if you plan to use it in production.

### Balance
Returns the address balance in BTC format (float like 0.00000001), or `null` if the cryptocurrency isn't supported or if there's no blockchain service available at the moment.

`GET /balance/{crypto}/{address}`

Example:

[`GET /balance/dash/Xe1M5THPzTwaegJF8njUP6sKRye3sm3Q5H`](https://scryp.herokuapp.com/balance/dash/Xe1M5THPzTwaegJF8njUP6sKRye3sm3Q5H)
```
{
	balance: 51.7033581
}
```

### Transaction

#### History
Returns a list of the address' transactions.

`GET /transaction/{crypto}/{address}`

Example:

[`GET /transaction/ltc/LWvWQ3XMoipFsAqE1EZPQFUovLea7DC1ef`](https://scryp.herokuapp.com/transaction/ltc/LWvWQ3XMoipFsAqE1EZPQFUovLea7DC1ef)
```
[{
		amount: 0.16624453,
		txid: "a912e05e6e882cc052bec85f0cc181cffffb55157c2a63b2738428b74a0128ac",
		date: 1518453499,
		confirmations: 4
	},
	{
		amount: 0.03834453,
		txid: "a912e05e6e882cc052bec85f0cc181cffffb55157c2a63b2738428b74a0128ac",
		date: 1518453499,
		confirmations: 4
	},
	{
		amount: 2.67377262,
		txid: "dc60b4ee5a74dbeafbc0a091d37fd94600b7bea37f086de046519c9ed45f43fc",
		date: 1518451180,
		confirmations: 21
	},
    ...
]
```

#### Single
Returns a single transaction by their TXID.

`GET /transaction/{crypto}/single/{txid}`

Example:

[`GET /transaction/bch/single/a8213e68c5cb2b6cfc192928dd1135068439e93819df852aade15f4c657a0542`](https://scryp.herokuapp.com/transaction/bch/single/a8213e68c5cb2b6cfc192928dd1135068439e93819df852aade15f4c657a0542)
```
{
	fee: 340,
	version: 1,
	txid: "a8213e68c5cb2b6cfc192928dd1135068439e93819df852aade15f4c657a0542",
	outputs: [{
		address: "1H7M7Zjg9SkDeVr3kCufM8yFC14Fs51bxB",
		amount: 158117428,
		scriptPubKey: "76a914b0b54c465013bb286e0016194c4e4eedbcdb08e988ac"
	}],
	inputs: [{
			txid: "32a87363920b622aa45831e5e0cadad6d392c5a7c149ede005e4ad45d186140d",
			scriptSig: "483045022100d0c5dabd2a2d8f0da52043b8e72d8a00ceb6addec65dc52638711fc3fca94ac902201af4b79e8ddb8586bf6a3c42c97c5ab55b5a7b5b0cdd076c54eda00846f3b0d9412102eddcf7af7b7824d593745c0235657b34eb610d866730c30f7c8b6bf5a82587a5",
			sequence: 4294967294,
			address: "1J5PxwjhjaWMMadC8sfmg6vfcF6c9XFXYX",
			amount: 99990000,
			n: 0
		},
		{
			txid: "e17bf7f129fadf7e03bc14b4e8b504edb78b578ccd2964323a88b8bcef7c610c",
			scriptSig: "483045022100819bd99cd2d8ecc28f718c38edc199e299206d6a8a2ea6e1e2985a796b3dffbf022013e8162ef2779c01043b8c232b684d844d8c09348bb2b8447f7c2764ce8752f6412102eddcf7af7b7824d593745c0235657b34eb610d866730c30f7c8b6bf5a82587a5",
			sequence: 4294967294,
			address: "1J5PxwjhjaWMMadC8sfmg6vfcF6c9XFXYX",
			amount: 58127768,
			n: 1
		}
	],
	time: 1518455788,
	confirmations: 2,
	locktime: 517105,
	size: 340,
	block_number: 517108
}
```

### Block

#### Latest
Returns the current block.

`GET /block/{crypto}`

Example:

[`GET /block/cloak`](https://scryp.herokuapp.com/block/cloak)
```
{
	previous_hash: "00000000000000000049ec93db50bdfb763d8c77eef7d9867b2e16eba8bc585c",
	next_hash: null,
	time: 1518456146,
	version: 536870912,
	hash: "00000000000000000057a4bc65c18f4535efcb82d370166ddabfb3fc664d445c",
	txids: [
		"62a07d23cf36708538c502c973683eb334ea8a91a95944f0e015d184735f12b4",
		"7a21a45b9c69729481dd70982acf2840e173e40fb3604a9a457e4a7bd6f81300",
		"867493b328beef46ae78c4730eca37f59647b0ab2f1e03177546d4c21c29377d",
        ...
	],
	block_number: 508848
}
```

#### By Hash
Returns a block by their hash.

`GET /block/{crypto}/{hash}`

Example:

[`GET /block/zec/00000000000000000030964e5f4f632e0f20e7c82cfc55acded63fd57dbe65c6`](https://scryp.herokuapp.com/block/zec/00000000000000000030964e5f4f632e0f20e7c82cfc55acded63fd57dbe65c6)
```
{
	previous_hash: "0000000000000000004056528bb847ff3e3d2c3124ddfddc7a56ad192e5c57dd",
	next_hash: null,
	time: 1518454111,
	version: 536870912,
	hash: "00000000000000000030964e5f4f632e0f20e7c82cfc55acded63fd57dbe65c6",
	txids: [
		"d9b65cac6dd83df80be5c01d09dfb787e899521db4aa7d087688fe78d5444e07",
		"87a53b7a45a5fcbe6e39a4210e78850a5de4eb1069d5fda63e480cfec8a982b9",
		"d154ba2694196b38cb10de3a43e1b7c72ce5cfaf46e05107f13eaac3382c1b67",
		...
	],
	block_number: 508845
}
```

### Price
If you need a more robust Price API take a look at the [CryptoCompare API](https://cryptocompare.com/api/), it's more complete and production ready!

#### To Crypto
Returns the current price from one cryptocurrency into another.

`GET /price/{crypto}/{crypto}`

Example:

[`GET /price/eth/btc`](https://scryp.herokuapp.com/price/eth/btc)
```
{
	price: 0.098933
}
```

#### To Fiat
Returns the current price from one cryptocurrency into a fiat currency.

`GET /price/{crypto}/{fiat}`

Example:

[`GET /price/eth/eur`](https://scryp.herokuapp.com/price/eth/eur)
```
{
	price: 688.75
}
```
