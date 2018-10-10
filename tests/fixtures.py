import json


parts_match_response = json.loads("""{
  "msec": 112,
  "request": {
    "exact_only": false,
    "__class__": "PartsMatchRequest",
    "queries": [
      {
        "q": "RUM001L02T2CL",
        "sku": null,
        "limit": 3,
        "reference": "RUM001L02T2CL",
        "mpn_or_sku": null,
        "mpn": null,
        "brand": null,
        "__class__": "PartsMatchQuery",
        "start": 0,
        "seller": null
      }
    ]
  },
  "__class__": "PartsMatchResponse",
  "results": [
    {
      "items": [
        {
          "offers": [
            {
              "sku": "RUM001L02T2CLTR-ND",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:36:54Z",
              "order_multiple": null,
              "in_stock_quantity": 152000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ea26cb&sid=459&ppid=24403092&vpid=99372901&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "c2ec7bf974bf15a02973e7a45c2a437c",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.05250"
                  ],
                  [
                    16000,
                    "0.04463"
                  ],
                  [
                    24000,
                    "0.04200"
                  ],
                  [
                    56000,
                    "0.03938"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLCT-ND",
              "packaging": "Cut Tape",
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:36:54Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=07e0e74&sid=459&ppid=24403092&vpid=99372899&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "d71ea09ec6069f030abb8a950866cadd",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLDKR-ND",
              "packaging": "Custom Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:36:54Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0788fbf&sid=459&ppid=24403092&vpid=99372900&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "7bd9a380f2023eabddf1260bb559e4d3",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "5070019",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-11T01:39:11Z",
              "order_multiple": 8000,
              "in_stock_quantity": 128000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CA",
                "has_ecommerce": true,
                "name": "Future Electronics",
                "__class__": "Seller",
                "homepage_url": "http:\/\/futureelectronics.com",
                "id": "2454",
                "uid": "e4032109c4f337c4"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=05fb6ca&sid=2454&ppid=24403092&vpid=416901410&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "039dd3f534b8c75f8673b46d1563560e",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03660"
                  ],
                  [
                    16000,
                    "0.03480"
                  ],
                  [
                    24000,
                    "0.03440"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T17:41:31Z",
              "order_multiple": null,
              "in_stock_quantity": 80000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ffb412&sid=5489&ppid=24403092&vpid=412212782&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.04260"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "755-RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T14:15:32Z",
              "order_multiple": null,
              "in_stock_quantity": 23270,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Mouser",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.mouser.com",
                "id": "2401",
                "uid": "a5e060ea85e77627"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec7611&sid=2401&ppid=24403092&vpid=177765296&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "209c9d280514fa60282deec06e8f3176",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.33000"
                  ],
                  [
                    10,
                    "0.22500"
                  ],
                  [
                    50,
                    "0.22500"
                  ],
                  [
                    100,
                    "0.09400"
                  ],
                  [
                    1000,
                    "0.06400"
                  ],
                  [
                    10000,
                    "0.04300"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T17:41:31Z",
              "order_multiple": null,
              "in_stock_quantity": 16800,
              "eligible_region": "",
              "moq": 497,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04f59a1&sid=5489&ppid=24403092&vpid=401812195&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    497,
                    "0.05040"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901109191",
              "packaging": "Bulk",
              "on_order_eta": null,
              "last_updated": "2017-03-12T10:52:21Z",
              "order_multiple": null,
              "in_stock_quantity": 16700,
              "eligible_region": "",
              "moq": 50,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Japan",
                "__class__": "Seller",
                "homepage_url": "http:\/\/chip1stop.com\/",
                "id": "4089",
                "uid": "90be55b4b6214379"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec05b5&sid=13512&ppid=24403092&vpid=279849046&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce52da5a8962778d6f7b23ee2ed80afd",
              "factory_lead_days": 1,
              "prices": {
                "JPY": [
                  [
                    50,
                    "4.48000"
                  ],
                  [
                    100,
                    "3.91000"
                  ],
                  [
                    500,
                    "3.21000"
                  ],
                  [
                    2000,
                    "2.75000"
                  ],
                  [
                    8000,
                    "2.66000"
                  ],
                  [
                    16000,
                    "2.64000"
                  ]
                ],
                "USD": [
                  [
                    50,
                    "0.03960"
                  ],
                  [
                    100,
                    "0.03460"
                  ],
                  [
                    500,
                    "0.02840"
                  ],
                  [
                    2000,
                    "0.02430"
                  ],
                  [
                    8000,
                    "0.02350"
                  ],
                  [
                    16000,
                    "0.02330"
                  ]
                ],
                "CNY": [
                  [
                    50,
                    "0.33000"
                  ],
                  [
                    100,
                    "0.29000"
                  ],
                  [
                    500,
                    "0.23000"
                  ],
                  [
                    2000,
                    "0.20000"
                  ],
                  [
                    8000,
                    "0.19000"
                  ],
                  [
                    16000,
                    "0.19000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901573642",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:33:19Z",
              "order_multiple": null,
              "in_stock_quantity": 5000,
              "eligible_region": "",
              "moq": 300,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Global",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.chip1stop.com",
                "id": "10930",
                "uid": "d2d317d9d1070114"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04fe7c0&sid=27109&ppid=24403092&vpid=268011108&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "f5bca64303f2035d30aa79422016a522",
              "factory_lead_days": 2,
              "prices": {
                "JPY": [
                  [
                    300,
                    "19.60000"
                  ],
                  [
                    600,
                    "18.70000"
                  ],
                  [
                    1200,
                    "17.90000"
                  ],
                  [
                    2100,
                    "16.60000"
                  ]
                ],
                "USD": [
                  [
                    300,
                    "0.17600"
                  ],
                  [
                    600,
                    "0.16800"
                  ],
                  [
                    1200,
                    "0.16100"
                  ],
                  [
                    2100,
                    "0.14900"
                  ]
                ],
                "CNY": [
                  [
                    300,
                    "1.43000"
                  ],
                  [
                    600,
                    "1.36000"
                  ],
                  [
                    1200,
                    "1.30000"
                  ],
                  [
                    2100,
                    "1.21000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-01T03:29:39Z",
              "order_multiple": 1,
              "in_stock_quantity": 100,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CN",
                "has_ecommerce": true,
                "name": "Ameya360",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.ameya360.com\/",
                "id": "11104",
                "uid": "6c5ca9566e5abf9b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0bc185a&sid=27291&ppid=24403092&vpid=418112693&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "5efe6eb18432aab1c68cfe8b2803f3d8",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.35000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-10T22:18:05Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Avnet",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com",
                "id": "2628",
                "uid": "3667f36d1545e5a0"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0a69187&sid=5822&ppid=24403092&vpid=54000614&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "3c3d78d05d7f78d743fc49e843806d3d",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03956"
                  ],
                  [
                    16000,
                    "0.03709"
                  ],
                  [
                    32000,
                    "0.03492"
                  ],
                  [
                    48000,
                    "0.03298"
                  ],
                  [
                    80000,
                    "0.03209"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T12:14:32Z",
              "order_multiple": null,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "TTI",
                "__class__": "Seller",
                "homepage_url": "https:\/\/www.ttiinc.com",
                "id": "950",
                "uid": "75dcb0d65f0ca61b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0f2869c&sid=950&ppid=24403092&vpid=259663955&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1c41fa443653d8589a326283aab5b04b",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T06:06:40Z",
              "order_multiple": null,
              "in_stock_quantity": 48,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "Farnell",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.farnell.com\/",
                "id": "819",
                "uid": "58989d9272cd8b5f"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0985061&sid=819&ppid=24403092&vpid=413510374&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce943698838bf7a5fb82fd652bdcaeb6",
              "factory_lead_days": null,
              "prices": {
                "GBP": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ],
                  [
                    1000,
                    "0.05000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T08:37:03Z",
              "order_multiple": null,
              "in_stock_quantity": 70,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "element14 APAC",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.element14.com\/",
                "id": "3702",
                "uid": "7f61ba6b5871aca6"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ca0e35&sid=11744&ppid=24403092&vpid=413514237&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2d9fcccd64294e03de71d28446e4fc41",
              "factory_lead_days": null,
              "prices": {
                "SGD": [
                  [
                    1,
                    "0.46800"
                  ],
                  [
                    10,
                    "0.32000"
                  ],
                  [
                    100,
                    "0.13500"
                  ],
                  [
                    250,
                    "0.10400"
                  ],
                  [
                    500,
                    "0.09700"
                  ],
                  [
                    1000,
                    "0.09000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T07:13:50Z",
              "order_multiple": 1,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "EU",
                "has_ecommerce": true,
                "name": "Avnet Europe",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?storeId=500201&action=home&region=EMEA&catalogId=500201&langId=-1",
                "id": "5347",
                "uid": "9416511ca99347d1"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04bb831&sid=15544&ppid=24403092&vpid=265726863&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2e3c9d13b122d0eb9e6ab3d64dd92283",
              "factory_lead_days": 84,
              "prices": {
                "EUR": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2C",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T06:28:23Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0e012d5&sid=14182&ppid=24403092&vpid=274748405&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "e093263319765471cc037fe53a017ff1",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03143"
                  ],
                  [
                    16000,
                    "0.02973"
                  ],
                  [
                    32000,
                    "0.02895"
                  ],
                  [
                    48000,
                    "0.02444"
                  ],
                  [
                    80000,
                    "0.02200"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T06:28:23Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0175410&sid=14182&ppid=24403092&vpid=179081466&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "10d7c4aba0c53356f88cc7cfac7979cf",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.04850"
                  ],
                  [
                    16000,
                    "0.04006"
                  ],
                  [
                    32000,
                    "0.03880"
                  ],
                  [
                    48000,
                    "0.03696"
                  ],
                  [
                    80000,
                    "0.03637"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "1246838",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-02-28T12:06:30Z",
              "order_multiple": null,
              "in_stock_quantity": 7800,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "RS Components",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.rs-components.com",
                "id": "3261",
                "uid": "fbaa3ea0de71286d"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=01dc8df&sid=10022&ppid=24403092&vpid=277797924&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "be8d08654390ea0f5a9467e1ff79c921",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T11:16:15Z",
              "order_multiple": null,
              "in_stock_quantity": 3434,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Quest",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.questcomp.com",
                "id": "2412",
                "uid": "b29977939293615e"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0c8f42d&sid=2412&ppid=24403092&vpid=237424745&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "69551c6692ea6ff32ee603a4cd9fd4f1",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.15000"
                  ],
                  [
                    34,
                    "0.12000"
                  ],
                  [
                    84,
                    "0.07500"
                  ],
                  [
                    668,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": false,
              "is_realtime": false
            }
          ],
          "uid": "cdf0058eb4021237",
          "mpn": "RUM001L02T2CL",
          "redirected_uids": [

          ],
          "brand": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Brand",
            "name": "Rohm",
            "uid": "12f2d3f83daac535"
          },
          "octopart_url": "https:\/\/octopart.com\/rum001l02t2cl-rohm-24403092",
          "__class__": "Part",
          "manufacturer": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Manufacturer",
            "name": "Rohm",
            "uid": "23ede6e708b5f02a"
          }
        }
      ],
      "hits": 1,
      "__class__": "PartsMatchResult",
      "reference": "RUM001L02T2CL",
      "error": null
    }
  ]
}""")


parts_match_extra_fields_response = json.loads("""{
  "msec": 58,
  "request": {
    "exact_only": false,
    "__class__": "PartsMatchRequest",
    "queries": [
      {
        "q": "RUM001L02T2CL",
        "sku": null,
        "limit": 3,
        "reference": "RUM001L02T2CL",
        "mpn_or_sku": null,
        "mpn": null,
        "brand": null,
        "__class__": "PartsMatchQuery",
        "start": 0,
        "seller": null
      }
    ]
  },
  "__class__": "PartsMatchResponse",
  "results": [
    {
      "items": [
        {
          "uid": "cdf0058eb4021237",
          "mpn": "RUM001L02T2CL",
          "brand": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Brand",
            "name": "Rohm",
            "uid": "12f2d3f83daac535"
          },
          "descriptions": [
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "element14 APAC",
                    "uid": "cdc808c2c94e1e0f"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "MOSFET, N-CH, 20V, 0.1A, VMT"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Avnet Europe",
                    "uid": "a7c762cdb2197400"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "Trans MOSFET N-CH 20V 0.1A 3-Pin VMT T\/R"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "RS Components",
                    "uid": "322cf7263c6ce1eb"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "MOSFET N-channel 20V 100mA SOT723"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Digi-Key",
                    "uid": "2c3be9310496fffc"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "MOSFET N-CH 20V 0.1A VMT3"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Verical",
                    "uid": "3c6cf966007befab"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "Trans MOSFET N-CH 20V 0.1A 3-Pin VMT T\/R"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Farnell",
                    "uid": "58989d9272cd8b5f"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "MOSFET, N-CH, 20V, 0.1A, VMT"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Avnet Asia",
                    "uid": "547e91744a7e87b9"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "Trans MOSFET N-CH 20V 0.1A 3-Pin VMT T\/R"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Avnet",
                    "uid": "c1e404eefe3c1223"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "Trans MOSFET N-CH 20V 0.1A 3-Pin VMT T\/R"
            },
            {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Future Electronics",
                    "uid": "e4032109c4f337c4"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "__class__": "Description",
              "value": "RUM001L02 Series 20 V 3.5 Ohm 100 mA N-Ch. Small Signal Mosfet - SOT-723 (VMT3)"
            }
          ],
          "specs": {
            "packaging": {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Ciiva",
                    "uid": "8c5c4956cfa65f9b"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "max_value": null,
              "min_value": null,
              "__class__": "SpecValue",
              "value": [
                "Tape & Reel (TR)"
              ],
              "display_value": "Tape & Reel (TR)",
              "metadata": {
                "datatype": "string",
                "unit": null,
                "__class__": "SpecMetadata",
                "key": "packaging",
                "name": "Packaging"
              }
            },
            "rohs_status": {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Farnell",
                    "uid": "58989d9272cd8b5f"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "max_value": null,
              "min_value": null,
              "__class__": "SpecValue",
              "value": [
                "Compliant"
              ],
              "display_value": "Compliant",
              "metadata": {
                "datatype": "string",
                "unit": null,
                "__class__": "SpecMetadata",
                "key": "rohs_status",
                "name": "RoHS"
              }
            },
            "lead_free_status": {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Future Electronics",
                    "uid": "e4032109c4f337c4"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "max_value": null,
              "min_value": null,
              "__class__": "SpecValue",
              "value": [
                "Lead Free"
              ],
              "display_value": "Lead Free",
              "metadata": {
                "datatype": "string",
                "unit": null,
                "__class__": "SpecMetadata",
                "key": "lead_free_status",
                "name": "Lead-Free Status"
              }
            },
            "mounting_style": {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Ciiva",
                    "uid": "8c5c4956cfa65f9b"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "max_value": null,
              "min_value": null,
              "__class__": "SpecValue",
              "value": [
                "Surface Mount"
              ],
              "display_value": "Surface Mount",
              "metadata": {
                "datatype": "string",
                "unit": null,
                "__class__": "SpecMetadata",
                "key": "mounting_style",
                "name": "Mounting Style"
              }
            },
            "polarity": {
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "element14 APAC",
                    "uid": "cdc808c2c94e1e0f"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "max_value": null,
              "min_value": null,
              "__class__": "SpecValue",
              "value": [
                "N-Channel"
              ],
              "display_value": "N-Channel",
              "metadata": {
                "datatype": "string",
                "unit": null,
                "__class__": "SpecMetadata",
                "key": "polarity",
                "name": "Polarity"
              }
            }
          },
          "manufacturer": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Manufacturer",
            "name": "Rohm",
            "uid": "23ede6e708b5f02a"
          },
          "imagesets": [
            {
              "medium_image": {
                "url": "https:\/\/sigma.octopart.com\/67745388\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "large_image": null,
              "credit_string": "element14 APAC",
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "element14 APAC",
                    "uid": "cdc808c2c94e1e0f"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "small_image": {
                "url": "https:\/\/sigma.octopart.com\/66829790\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "__class__": "ImageSet",
              "swatch_image": {
                "url": "https:\/\/sigma.octopart.com\/23299222\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "credit_url": "http:\/\/www.element14.com\/"
            },
            {
              "medium_image": {
                "url": "https:\/\/sigma.octopart.com\/67745388\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "large_image": null,
              "credit_string": "Farnell",
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Farnell",
                    "uid": "58989d9272cd8b5f"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "small_image": {
                "url": "https:\/\/sigma.octopart.com\/66829790\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "__class__": "ImageSet",
              "swatch_image": {
                "url": "https:\/\/sigma.octopart.com\/23299222\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "credit_url": "http:\/\/www.farnell.com\/"
            },
            {
              "medium_image": {
                "url": "https:\/\/sigma.octopart.com\/78444059\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "large_image": {
                "url": "https:\/\/sigma.octopart.com\/78444063\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "credit_string": "Ameya360",
              "attribution": {
                "sources": [
                  {
                    "__class__": "Source",
                    "name": "Ameya360",
                    "uid": "e16e2464a29332a9"
                  }
                ],
                "__class__": "Attribution",
                "first_acquired": null
              },
              "small_image": {
                "url": "https:\/\/sigma.octopart.com\/78444048\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "__class__": "ImageSet",
              "swatch_image": {
                "url": "https:\/\/sigma.octopart.com\/78444042\/image\/Rohm-RUM001L02T2CL.jpg",
                "mimetype": "image\/jpg",
                "__class__": "Asset",
                "metadata": {
                  "width": null,
                  "height": null
                }
              },
              "credit_url": "http:\/\/www.ameya360.com\/"
            }
          ],
          "redirected_uids": [

          ],
          "__class__": "Part",
          "offers": [
            {
              "sku": "RUM001L02T2CLTR-ND",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:36:54Z",
              "order_multiple": null,
              "in_stock_quantity": 152000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ea26cb&sid=459&ppid=24403092&vpid=99372901&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "c2ec7bf974bf15a02973e7a45c2a437c",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.05250"
                  ],
                  [
                    16000,
                    "0.04463"
                  ],
                  [
                    24000,
                    "0.04200"
                  ],
                  [
                    56000,
                    "0.03938"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLDKR-ND",
              "packaging": "Custom Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:36:54Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0788fbf&sid=459&ppid=24403092&vpid=99372900&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "7bd9a380f2023eabddf1260bb559e4d3",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLCT-ND",
              "packaging": "Cut Tape",
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:36:54Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=07e0e74&sid=459&ppid=24403092&vpid=99372899&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "d71ea09ec6069f030abb8a950866cadd",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "5070019",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-11T01:39:11Z",
              "order_multiple": 8000,
              "in_stock_quantity": 128000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CA",
                "has_ecommerce": true,
                "name": "Future Electronics",
                "__class__": "Seller",
                "homepage_url": "http:\/\/futureelectronics.com",
                "id": "2454",
                "uid": "e4032109c4f337c4"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=05fb6ca&sid=2454&ppid=24403092&vpid=416901410&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "039dd3f534b8c75f8673b46d1563560e",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03660"
                  ],
                  [
                    16000,
                    "0.03480"
                  ],
                  [
                    24000,
                    "0.03440"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T17:41:31Z",
              "order_multiple": null,
              "in_stock_quantity": 80000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ffb412&sid=5489&ppid=24403092&vpid=412212782&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.04260"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "755-RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T14:15:32Z",
              "order_multiple": null,
              "in_stock_quantity": 23270,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Mouser",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.mouser.com",
                "id": "2401",
                "uid": "a5e060ea85e77627"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec7611&sid=2401&ppid=24403092&vpid=177765296&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "209c9d280514fa60282deec06e8f3176",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.33000"
                  ],
                  [
                    10,
                    "0.22500"
                  ],
                  [
                    50,
                    "0.22500"
                  ],
                  [
                    100,
                    "0.09400"
                  ],
                  [
                    1000,
                    "0.06400"
                  ],
                  [
                    10000,
                    "0.04300"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T17:41:31Z",
              "order_multiple": null,
              "in_stock_quantity": 16800,
              "eligible_region": "",
              "moq": 497,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04f59a1&sid=5489&ppid=24403092&vpid=401812195&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    497,
                    "0.05040"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901109191",
              "packaging": "Bulk",
              "on_order_eta": null,
              "last_updated": "2017-03-12T10:52:21Z",
              "order_multiple": null,
              "in_stock_quantity": 16700,
              "eligible_region": "",
              "moq": 50,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Japan",
                "__class__": "Seller",
                "homepage_url": "http:\/\/chip1stop.com\/",
                "id": "4089",
                "uid": "90be55b4b6214379"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec05b5&sid=13512&ppid=24403092&vpid=279849046&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce52da5a8962778d6f7b23ee2ed80afd",
              "factory_lead_days": 1,
              "prices": {
                "JPY": [
                  [
                    50,
                    "4.48000"
                  ],
                  [
                    100,
                    "3.91000"
                  ],
                  [
                    500,
                    "3.21000"
                  ],
                  [
                    2000,
                    "2.75000"
                  ],
                  [
                    8000,
                    "2.66000"
                  ],
                  [
                    16000,
                    "2.64000"
                  ]
                ],
                "USD": [
                  [
                    50,
                    "0.03960"
                  ],
                  [
                    100,
                    "0.03460"
                  ],
                  [
                    500,
                    "0.02840"
                  ],
                  [
                    2000,
                    "0.02430"
                  ],
                  [
                    8000,
                    "0.02350"
                  ],
                  [
                    16000,
                    "0.02330"
                  ]
                ],
                "CNY": [
                  [
                    50,
                    "0.33000"
                  ],
                  [
                    100,
                    "0.29000"
                  ],
                  [
                    500,
                    "0.23000"
                  ],
                  [
                    2000,
                    "0.20000"
                  ],
                  [
                    8000,
                    "0.19000"
                  ],
                  [
                    16000,
                    "0.19000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901573642",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T12:33:19Z",
              "order_multiple": null,
              "in_stock_quantity": 5000,
              "eligible_region": "",
              "moq": 300,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Global",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.chip1stop.com",
                "id": "10930",
                "uid": "d2d317d9d1070114"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04fe7c0&sid=27109&ppid=24403092&vpid=268011108&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "f5bca64303f2035d30aa79422016a522",
              "factory_lead_days": 2,
              "prices": {
                "JPY": [
                  [
                    300,
                    "19.60000"
                  ],
                  [
                    600,
                    "18.70000"
                  ],
                  [
                    1200,
                    "17.90000"
                  ],
                  [
                    2100,
                    "16.60000"
                  ]
                ],
                "USD": [
                  [
                    300,
                    "0.17600"
                  ],
                  [
                    600,
                    "0.16800"
                  ],
                  [
                    1200,
                    "0.16100"
                  ],
                  [
                    2100,
                    "0.14900"
                  ]
                ],
                "CNY": [
                  [
                    300,
                    "1.43000"
                  ],
                  [
                    600,
                    "1.36000"
                  ],
                  [
                    1200,
                    "1.30000"
                  ],
                  [
                    2100,
                    "1.21000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-01T03:29:39Z",
              "order_multiple": 1,
              "in_stock_quantity": 100,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CN",
                "has_ecommerce": true,
                "name": "Ameya360",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.ameya360.com\/",
                "id": "11104",
                "uid": "6c5ca9566e5abf9b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0bc185a&sid=27291&ppid=24403092&vpid=418112693&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "5efe6eb18432aab1c68cfe8b2803f3d8",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.35000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-10T22:18:05Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Avnet",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com",
                "id": "2628",
                "uid": "3667f36d1545e5a0"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0a69187&sid=5822&ppid=24403092&vpid=54000614&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "3c3d78d05d7f78d743fc49e843806d3d",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03956"
                  ],
                  [
                    16000,
                    "0.03709"
                  ],
                  [
                    32000,
                    "0.03492"
                  ],
                  [
                    48000,
                    "0.03298"
                  ],
                  [
                    80000,
                    "0.03209"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T12:14:32Z",
              "order_multiple": null,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "TTI",
                "__class__": "Seller",
                "homepage_url": "https:\/\/www.ttiinc.com",
                "id": "950",
                "uid": "75dcb0d65f0ca61b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0f2869c&sid=950&ppid=24403092&vpid=259663955&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1c41fa443653d8589a326283aab5b04b",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T06:06:40Z",
              "order_multiple": null,
              "in_stock_quantity": 48,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "Farnell",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.farnell.com\/",
                "id": "819",
                "uid": "58989d9272cd8b5f"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0985061&sid=819&ppid=24403092&vpid=413510374&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce943698838bf7a5fb82fd652bdcaeb6",
              "factory_lead_days": null,
              "prices": {
                "GBP": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ],
                  [
                    1000,
                    "0.05000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T08:37:03Z",
              "order_multiple": null,
              "in_stock_quantity": 70,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "element14 APAC",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.element14.com\/",
                "id": "3702",
                "uid": "7f61ba6b5871aca6"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ca0e35&sid=11744&ppid=24403092&vpid=413514237&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2d9fcccd64294e03de71d28446e4fc41",
              "factory_lead_days": null,
              "prices": {
                "SGD": [
                  [
                    1,
                    "0.46800"
                  ],
                  [
                    10,
                    "0.32000"
                  ],
                  [
                    100,
                    "0.13500"
                  ],
                  [
                    250,
                    "0.10400"
                  ],
                  [
                    500,
                    "0.09700"
                  ],
                  [
                    1000,
                    "0.09000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T07:13:50Z",
              "order_multiple": 1,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "EU",
                "has_ecommerce": true,
                "name": "Avnet Europe",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?storeId=500201&action=home&region=EMEA&catalogId=500201&langId=-1",
                "id": "5347",
                "uid": "9416511ca99347d1"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04bb831&sid=15544&ppid=24403092&vpid=265726863&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2e3c9d13b122d0eb9e6ab3d64dd92283",
              "factory_lead_days": 84,
              "prices": {
                "EUR": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2C",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T06:28:23Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0e012d5&sid=14182&ppid=24403092&vpid=274748405&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "e093263319765471cc037fe53a017ff1",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03143"
                  ],
                  [
                    16000,
                    "0.02973"
                  ],
                  [
                    32000,
                    "0.02895"
                  ],
                  [
                    48000,
                    "0.02444"
                  ],
                  [
                    80000,
                    "0.02200"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-12T06:28:23Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0175410&sid=14182&ppid=24403092&vpid=179081466&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "10d7c4aba0c53356f88cc7cfac7979cf",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.04850"
                  ],
                  [
                    16000,
                    "0.04006"
                  ],
                  [
                    32000,
                    "0.03880"
                  ],
                  [
                    48000,
                    "0.03696"
                  ],
                  [
                    80000,
                    "0.03637"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "1246838",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-02-28T12:06:30Z",
              "order_multiple": null,
              "in_stock_quantity": 7800,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "RS Components",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.rs-components.com",
                "id": "3261",
                "uid": "fbaa3ea0de71286d"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=01dc8df&sid=10022&ppid=24403092&vpid=277797924&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "be8d08654390ea0f5a9467e1ff79c921",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-11T11:16:15Z",
              "order_multiple": null,
              "in_stock_quantity": 3434,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Quest",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.questcomp.com",
                "id": "2412",
                "uid": "b29977939293615e"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0c8f42d&sid=2412&ppid=24403092&vpid=237424745&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "69551c6692ea6ff32ee603a4cd9fd4f1",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.15000"
                  ],
                  [
                    34,
                    "0.12000"
                  ],
                  [
                    84,
                    "0.07500"
                  ],
                  [
                    668,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": false,
              "is_realtime": false
            }
          ],
          "octopart_url": "https:\/\/octopart.com\/rum001l02t2cl-rohm-24403092"
        }
      ],
      "hits": 1,
      "__class__": "PartsMatchResult",
      "reference": "RUM001L02T2CL",
      "error": null
    }
  ]
}""")


parts_match_multiple_sellers_response = json.loads("""{
  "msec": 173,
  "request": {
    "exact_only": false,
    "__class__": "PartsMatchRequest",
    "queries": [
      {
        "q": "RUM001L02T2CL",
        "sku": null,
        "limit": 3,
        "reference": "RUM001L02T2CL",
        "mpn_or_sku": null,
        "mpn": null,
        "brand": null,
        "__class__": "PartsMatchQuery",
        "start": 0,
        "seller": "Digi-Key"
      },
      {
        "q": "RUM001L02T2CL",
        "sku": null,
        "limit": 3,
        "reference": "RUM001L02T2CL",
        "mpn_or_sku": null,
        "mpn": null,
        "brand": null,
        "__class__": "PartsMatchQuery",
        "start": 0,
        "seller": "Mouser"
      }
    ]
  },
  "__class__": "PartsMatchResponse",
  "results": [
    {
      "items": [
        {
          "offers": [
            {
              "sku": "RUM001L02T2CLTR-ND",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-14T12:33:22Z",
              "order_multiple": null,
              "in_stock_quantity": 152000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ea26cb&sid=459&ppid=24403092&vpid=99372901&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "c2ec7bf974bf15a02973e7a45c2a437c",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.05250"
                  ],
                  [
                    16000,
                    "0.04463"
                  ],
                  [
                    24000,
                    "0.04200"
                  ],
                  [
                    56000,
                    "0.03938"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLCT-ND",
              "packaging": "Cut Tape",
              "on_order_eta": null,
              "last_updated": "2017-03-14T12:33:22Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=07e0e74&sid=459&ppid=24403092&vpid=99372899&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "d71ea09ec6069f030abb8a950866cadd",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLDKR-ND",
              "packaging": "Custom Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-14T12:33:22Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0788fbf&sid=459&ppid=24403092&vpid=99372900&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "7bd9a380f2023eabddf1260bb559e4d3",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "5070019",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-14T00:39:18Z",
              "order_multiple": 8000,
              "in_stock_quantity": 128000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CA",
                "has_ecommerce": true,
                "name": "Future Electronics",
                "__class__": "Seller",
                "homepage_url": "http:\/\/futureelectronics.com",
                "id": "2454",
                "uid": "e4032109c4f337c4"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=05fb6ca&sid=2454&ppid=24403092&vpid=416901410&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "039dd3f534b8c75f8673b46d1563560e",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03660"
                  ],
                  [
                    16000,
                    "0.03480"
                  ],
                  [
                    24000,
                    "0.03440"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T17:41:44Z",
              "order_multiple": null,
              "in_stock_quantity": 80000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ffb412&sid=5489&ppid=24403092&vpid=412212782&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.04260"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901109191",
              "packaging": "Bulk",
              "on_order_eta": null,
              "last_updated": "2017-03-14T11:34:27Z",
              "order_multiple": null,
              "in_stock_quantity": 48700,
              "eligible_region": "",
              "moq": 50,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Japan",
                "__class__": "Seller",
                "homepage_url": "http:\/\/chip1stop.com\/",
                "id": "4089",
                "uid": "90be55b4b6214379"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec05b5&sid=13512&ppid=24403092&vpid=279849046&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce52da5a8962778d6f7b23ee2ed80afd",
              "factory_lead_days": 1,
              "prices": {
                "JPY": [
                  [
                    50,
                    "4.48000"
                  ],
                  [
                    100,
                    "3.91000"
                  ],
                  [
                    500,
                    "3.21000"
                  ],
                  [
                    2000,
                    "2.75000"
                  ],
                  [
                    8000,
                    "2.66000"
                  ],
                  [
                    16000,
                    "2.64000"
                  ]
                ],
                "USD": [
                  [
                    50,
                    "0.03960"
                  ],
                  [
                    100,
                    "0.03460"
                  ],
                  [
                    500,
                    "0.02840"
                  ],
                  [
                    2000,
                    "0.02430"
                  ],
                  [
                    8000,
                    "0.02350"
                  ],
                  [
                    16000,
                    "0.02330"
                  ]
                ],
                "CNY": [
                  [
                    50,
                    "0.33000"
                  ],
                  [
                    100,
                    "0.29000"
                  ],
                  [
                    500,
                    "0.23000"
                  ],
                  [
                    2000,
                    "0.20000"
                  ],
                  [
                    8000,
                    "0.19000"
                  ],
                  [
                    16000,
                    "0.19000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "755-RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T13:32:23Z",
              "order_multiple": null,
              "in_stock_quantity": 23270,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Mouser",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.mouser.com",
                "id": "2401",
                "uid": "a5e060ea85e77627"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec7611&sid=2401&ppid=24403092&vpid=177765296&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "209c9d280514fa60282deec06e8f3176",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.33000"
                  ],
                  [
                    10,
                    "0.22500"
                  ],
                  [
                    50,
                    "0.22500"
                  ],
                  [
                    100,
                    "0.09400"
                  ],
                  [
                    1000,
                    "0.06400"
                  ],
                  [
                    10000,
                    "0.04300"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T17:41:44Z",
              "order_multiple": null,
              "in_stock_quantity": 16800,
              "eligible_region": "",
              "moq": 497,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04f59a1&sid=5489&ppid=24403092&vpid=401812195&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    497,
                    "0.05040"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901573642",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T13:10:51Z",
              "order_multiple": null,
              "in_stock_quantity": 5000,
              "eligible_region": "",
              "moq": 300,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Global",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.chip1stop.com",
                "id": "10930",
                "uid": "d2d317d9d1070114"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04fe7c0&sid=27109&ppid=24403092&vpid=268011108&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "f5bca64303f2035d30aa79422016a522",
              "factory_lead_days": 2,
              "prices": {
                "JPY": [
                  [
                    300,
                    "19.60000"
                  ],
                  [
                    600,
                    "18.70000"
                  ],
                  [
                    1200,
                    "17.90000"
                  ],
                  [
                    2100,
                    "16.60000"
                  ]
                ],
                "USD": [
                  [
                    300,
                    "0.17600"
                  ],
                  [
                    600,
                    "0.16800"
                  ],
                  [
                    1200,
                    "0.16100"
                  ],
                  [
                    2100,
                    "0.14900"
                  ]
                ],
                "CNY": [
                  [
                    300,
                    "1.43000"
                  ],
                  [
                    600,
                    "1.36000"
                  ],
                  [
                    1200,
                    "1.30000"
                  ],
                  [
                    2100,
                    "1.21000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-01T03:29:39Z",
              "order_multiple": 1,
              "in_stock_quantity": 100,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CN",
                "has_ecommerce": true,
                "name": "Ameya360",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.ameya360.com\/",
                "id": "11104",
                "uid": "6c5ca9566e5abf9b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0bc185a&sid=27291&ppid=24403092&vpid=418112693&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "5efe6eb18432aab1c68cfe8b2803f3d8",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.35000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-13T22:22:23Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Avnet",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com",
                "id": "2628",
                "uid": "3667f36d1545e5a0"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0a69187&sid=5822&ppid=24403092&vpid=54000614&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "3c3d78d05d7f78d743fc49e843806d3d",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03956"
                  ],
                  [
                    16000,
                    "0.03709"
                  ],
                  [
                    32000,
                    "0.03492"
                  ],
                  [
                    48000,
                    "0.03298"
                  ],
                  [
                    80000,
                    "0.03209"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T09:14:34Z",
              "order_multiple": null,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "TTI",
                "__class__": "Seller",
                "homepage_url": "https:\/\/www.ttiinc.com",
                "id": "950",
                "uid": "75dcb0d65f0ca61b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0f2869c&sid=950&ppid=24403092&vpid=259663955&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1c41fa443653d8589a326283aab5b04b",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T06:39:53Z",
              "order_multiple": 8000,
              "in_stock_quantity": 40000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0dd95f1&sid=14182&ppid=24403092&vpid=179081466&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "10d7c4aba0c53356f88cc7cfac7979cf",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03858"
                  ],
                  [
                    16000,
                    "0.03849"
                  ],
                  [
                    32000,
                    "0.03839"
                  ],
                  [
                    48000,
                    "0.03829"
                  ],
                  [
                    80000,
                    "0.03820"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T18:03:55Z",
              "order_multiple": null,
              "in_stock_quantity": 48,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "Farnell",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.farnell.com\/",
                "id": "819",
                "uid": "58989d9272cd8b5f"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0985061&sid=819&ppid=24403092&vpid=413510374&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce943698838bf7a5fb82fd652bdcaeb6",
              "factory_lead_days": null,
              "prices": {
                "GBP": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ],
                  [
                    1000,
                    "0.05000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T18:48:01Z",
              "order_multiple": null,
              "in_stock_quantity": 48,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "element14 APAC",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.element14.com\/",
                "id": "3702",
                "uid": "7f61ba6b5871aca6"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ca0e35&sid=11744&ppid=24403092&vpid=413514237&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2d9fcccd64294e03de71d28446e4fc41",
              "factory_lead_days": null,
              "prices": {
                "SGD": [
                  [
                    1,
                    "0.46800"
                  ],
                  [
                    10,
                    "0.32000"
                  ],
                  [
                    100,
                    "0.13500"
                  ],
                  [
                    250,
                    "0.10400"
                  ],
                  [
                    500,
                    "0.09700"
                  ],
                  [
                    1000,
                    "0.09000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T07:16:16Z",
              "order_multiple": 1,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "EU",
                "has_ecommerce": true,
                "name": "Avnet Europe",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?storeId=500201&action=home&region=EMEA&catalogId=500201&langId=-1",
                "id": "5347",
                "uid": "9416511ca99347d1"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04bb831&sid=15544&ppid=24403092&vpid=265726863&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2e3c9d13b122d0eb9e6ab3d64dd92283",
              "factory_lead_days": 84,
              "prices": {
                "EUR": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2C",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T06:39:53Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0e012d5&sid=14182&ppid=24403092&vpid=274748405&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "e093263319765471cc037fe53a017ff1",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03143"
                  ],
                  [
                    16000,
                    "0.02973"
                  ],
                  [
                    32000,
                    "0.02895"
                  ],
                  [
                    48000,
                    "0.02444"
                  ],
                  [
                    80000,
                    "0.02200"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "1246838",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T14:39:45Z",
              "order_multiple": null,
              "in_stock_quantity": 8100,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "RS Components",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.rs-components.com",
                "id": "3261",
                "uid": "fbaa3ea0de71286d"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=01dc8df&sid=10022&ppid=24403092&vpid=277797924&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "be8d08654390ea0f5a9467e1ff79c921",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T19:12:09Z",
              "order_multiple": null,
              "in_stock_quantity": 3434,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Quest",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.questcomp.com",
                "id": "2412",
                "uid": "b29977939293615e"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0c8f42d&sid=2412&ppid=24403092&vpid=237424745&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "69551c6692ea6ff32ee603a4cd9fd4f1",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.15000"
                  ],
                  [
                    34,
                    "0.12000"
                  ],
                  [
                    84,
                    "0.07500"
                  ],
                  [
                    668,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": false,
              "is_realtime": false
            }
          ],
          "uid": "cdf0058eb4021237",
          "mpn": "RUM001L02T2CL",
          "redirected_uids": [

          ],
          "brand": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Brand",
            "name": "Rohm",
            "uid": "12f2d3f83daac535"
          },
          "octopart_url": "https:\/\/octopart.com\/rum001l02t2cl-rohm-24403092",
          "__class__": "Part",
          "manufacturer": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Manufacturer",
            "name": "Rohm",
            "uid": "23ede6e708b5f02a"
          }
        }
      ],
      "hits": 1,
      "__class__": "PartsMatchResult",
      "reference": "RUM001L02T2CL",
      "error": null
    },
    {
      "items": [
        {
          "offers": [
            {
              "sku": "RUM001L02T2CLTR-ND",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-14T12:33:22Z",
              "order_multiple": null,
              "in_stock_quantity": 152000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ea26cb&sid=459&ppid=24403092&vpid=99372901&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "c2ec7bf974bf15a02973e7a45c2a437c",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.05250"
                  ],
                  [
                    16000,
                    "0.04463"
                  ],
                  [
                    24000,
                    "0.04200"
                  ],
                  [
                    56000,
                    "0.03938"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLDKR-ND",
              "packaging": "Custom Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-14T12:33:22Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0788fbf&sid=459&ppid=24403092&vpid=99372900&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "7bd9a380f2023eabddf1260bb559e4d3",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CLCT-ND",
              "packaging": "Cut Tape",
              "on_order_eta": null,
              "last_updated": "2017-03-14T12:33:22Z",
              "order_multiple": null,
              "in_stock_quantity": 154976,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Digi-Key",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.digikey.com",
                "id": "459",
                "uid": "2c3be9310496fffc"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=07e0e74&sid=459&ppid=24403092&vpid=99372899&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "d71ea09ec6069f030abb8a950866cadd",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.37000"
                  ],
                  [
                    10,
                    "0.33800"
                  ],
                  [
                    25,
                    "0.24320"
                  ],
                  [
                    100,
                    "0.18930"
                  ],
                  [
                    250,
                    "0.11896"
                  ],
                  [
                    500,
                    "0.10140"
                  ],
                  [
                    1000,
                    "0.06895"
                  ],
                  [
                    2500,
                    "0.06219"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "5070019",
              "packaging": "Tape & Reel",
              "on_order_eta": null,
              "last_updated": "2017-03-14T00:39:18Z",
              "order_multiple": 8000,
              "in_stock_quantity": 128000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CA",
                "has_ecommerce": true,
                "name": "Future Electronics",
                "__class__": "Seller",
                "homepage_url": "http:\/\/futureelectronics.com",
                "id": "2454",
                "uid": "e4032109c4f337c4"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=05fb6ca&sid=2454&ppid=24403092&vpid=416901410&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "039dd3f534b8c75f8673b46d1563560e",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03660"
                  ],
                  [
                    16000,
                    "0.03480"
                  ],
                  [
                    24000,
                    "0.03440"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T17:41:44Z",
              "order_multiple": null,
              "in_stock_quantity": 80000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ffb412&sid=5489&ppid=24403092&vpid=412212782&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.04260"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901109191",
              "packaging": "Bulk",
              "on_order_eta": null,
              "last_updated": "2017-03-14T11:34:27Z",
              "order_multiple": null,
              "in_stock_quantity": 48700,
              "eligible_region": "",
              "moq": 50,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Japan",
                "__class__": "Seller",
                "homepage_url": "http:\/\/chip1stop.com\/",
                "id": "4089",
                "uid": "90be55b4b6214379"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec05b5&sid=13512&ppid=24403092&vpid=279849046&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce52da5a8962778d6f7b23ee2ed80afd",
              "factory_lead_days": 1,
              "prices": {
                "JPY": [
                  [
                    50,
                    "4.48000"
                  ],
                  [
                    100,
                    "3.91000"
                  ],
                  [
                    500,
                    "3.21000"
                  ],
                  [
                    2000,
                    "2.75000"
                  ],
                  [
                    8000,
                    "2.66000"
                  ],
                  [
                    16000,
                    "2.64000"
                  ]
                ],
                "USD": [
                  [
                    50,
                    "0.03960"
                  ],
                  [
                    100,
                    "0.03460"
                  ],
                  [
                    500,
                    "0.02840"
                  ],
                  [
                    2000,
                    "0.02430"
                  ],
                  [
                    8000,
                    "0.02350"
                  ],
                  [
                    16000,
                    "0.02330"
                  ]
                ],
                "CNY": [
                  [
                    50,
                    "0.33000"
                  ],
                  [
                    100,
                    "0.29000"
                  ],
                  [
                    500,
                    "0.23000"
                  ],
                  [
                    2000,
                    "0.20000"
                  ],
                  [
                    8000,
                    "0.19000"
                  ],
                  [
                    16000,
                    "0.19000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "755-RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T13:32:23Z",
              "order_multiple": null,
              "in_stock_quantity": 23270,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Mouser",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.mouser.com",
                "id": "2401",
                "uid": "a5e060ea85e77627"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ec7611&sid=2401&ppid=24403092&vpid=177765296&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "209c9d280514fa60282deec06e8f3176",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.33000"
                  ],
                  [
                    10,
                    "0.22500"
                  ],
                  [
                    50,
                    "0.22500"
                  ],
                  [
                    100,
                    "0.09400"
                  ],
                  [
                    1000,
                    "0.06400"
                  ],
                  [
                    10000,
                    "0.04300"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T17:41:44Z",
              "order_multiple": null,
              "in_stock_quantity": 16800,
              "eligible_region": "",
              "moq": 497,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Verical",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.verical.com",
                "id": "2617",
                "uid": "504e954473118389"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04f59a1&sid=5489&ppid=24403092&vpid=401812195&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1e4e51b2a9dde7418b0d63f09b163cc5",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    497,
                    "0.05040"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "C1S625901573642",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T13:10:51Z",
              "order_multiple": null,
              "in_stock_quantity": 5000,
              "eligible_region": "",
              "moq": 300,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "JP",
                "has_ecommerce": true,
                "name": "Chip One Stop Global",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.chip1stop.com",
                "id": "10930",
                "uid": "d2d317d9d1070114"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04fe7c0&sid=27109&ppid=24403092&vpid=268011108&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "f5bca64303f2035d30aa79422016a522",
              "factory_lead_days": 2,
              "prices": {
                "JPY": [
                  [
                    300,
                    "19.60000"
                  ],
                  [
                    600,
                    "18.70000"
                  ],
                  [
                    1200,
                    "17.90000"
                  ],
                  [
                    2100,
                    "16.60000"
                  ]
                ],
                "USD": [
                  [
                    300,
                    "0.17600"
                  ],
                  [
                    600,
                    "0.16800"
                  ],
                  [
                    1200,
                    "0.16100"
                  ],
                  [
                    2100,
                    "0.14900"
                  ]
                ],
                "CNY": [
                  [
                    300,
                    "1.43000"
                  ],
                  [
                    600,
                    "1.36000"
                  ],
                  [
                    1200,
                    "1.30000"
                  ],
                  [
                    2100,
                    "1.21000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-01T03:29:39Z",
              "order_multiple": 1,
              "in_stock_quantity": 100,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "CN",
                "has_ecommerce": true,
                "name": "Ameya360",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.ameya360.com\/",
                "id": "11104",
                "uid": "6c5ca9566e5abf9b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0bc185a&sid=27291&ppid=24403092&vpid=418112693&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "5efe6eb18432aab1c68cfe8b2803f3d8",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.35000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-13T22:22:23Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Avnet",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com",
                "id": "2628",
                "uid": "3667f36d1545e5a0"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0a69187&sid=5822&ppid=24403092&vpid=54000614&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "3c3d78d05d7f78d743fc49e843806d3d",
              "factory_lead_days": 70,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03956"
                  ],
                  [
                    16000,
                    "0.03709"
                  ],
                  [
                    32000,
                    "0.03492"
                  ],
                  [
                    48000,
                    "0.03298"
                  ],
                  [
                    80000,
                    "0.03209"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T09:14:34Z",
              "order_multiple": null,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "TTI",
                "__class__": "Seller",
                "homepage_url": "https:\/\/www.ttiinc.com",
                "id": "950",
                "uid": "75dcb0d65f0ca61b"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0f2869c&sid=950&ppid=24403092&vpid=259663955&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "1c41fa443653d8589a326283aab5b04b",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T06:39:53Z",
              "order_multiple": 8000,
              "in_stock_quantity": 40000,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0dd95f1&sid=14182&ppid=24403092&vpid=179081466&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "10d7c4aba0c53356f88cc7cfac7979cf",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03858"
                  ],
                  [
                    16000,
                    "0.03849"
                  ],
                  [
                    32000,
                    "0.03839"
                  ],
                  [
                    48000,
                    "0.03829"
                  ],
                  [
                    80000,
                    "0.03820"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T18:03:55Z",
              "order_multiple": null,
              "in_stock_quantity": 48,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "Farnell",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.farnell.com\/",
                "id": "819",
                "uid": "58989d9272cd8b5f"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0985061&sid=819&ppid=24403092&vpid=413510374&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "ce943698838bf7a5fb82fd652bdcaeb6",
              "factory_lead_days": null,
              "prices": {
                "GBP": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ],
                  [
                    1000,
                    "0.05000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "2706687",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T18:48:01Z",
              "order_multiple": null,
              "in_stock_quantity": 48,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "element14 APAC",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.element14.com\/",
                "id": "3702",
                "uid": "7f61ba6b5871aca6"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ca0e35&sid=11744&ppid=24403092&vpid=413514237&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2d9fcccd64294e03de71d28446e4fc41",
              "factory_lead_days": null,
              "prices": {
                "SGD": [
                  [
                    1,
                    "0.46800"
                  ],
                  [
                    10,
                    "0.32000"
                  ],
                  [
                    100,
                    "0.13500"
                  ],
                  [
                    250,
                    "0.10400"
                  ],
                  [
                    500,
                    "0.09700"
                  ],
                  [
                    1000,
                    "0.09000"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T07:16:16Z",
              "order_multiple": 1,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 1,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "EU",
                "has_ecommerce": true,
                "name": "Avnet Europe",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?storeId=500201&action=home&region=EMEA&catalogId=500201&langId=-1",
                "id": "5347",
                "uid": "9416511ca99347d1"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04bb831&sid=15544&ppid=24403092&vpid=265726863&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "2e3c9d13b122d0eb9e6ab3d64dd92283",
              "factory_lead_days": 84,
              "prices": {
                "EUR": [
                  [
                    1,
                    "0.26000"
                  ],
                  [
                    10,
                    "0.17800"
                  ],
                  [
                    100,
                    "0.07500"
                  ],
                  [
                    250,
                    "0.05800"
                  ],
                  [
                    500,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2C",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T06:39:53Z",
              "order_multiple": 8000,
              "in_stock_quantity": 0,
              "eligible_region": "",
              "moq": 8000,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "SG",
                "has_ecommerce": true,
                "name": "Avnet Asia",
                "__class__": "Seller",
                "homepage_url": "http:\/\/avnetexpress.avnet.com\/store\/em\/EMController?langId=-1&storeId=500201&catalogId=500201&action=home",
                "id": "4523",
                "uid": "8604430ebec955c3"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?c=1&country=US&ak=a8cfd5a0&sig=0e012d5&sid=14182&ppid=24403092&vpid=274748405&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "e093263319765471cc037fe53a017ff1",
              "factory_lead_days": 90,
              "prices": {
                "USD": [
                  [
                    8000,
                    "0.03143"
                  ],
                  [
                    16000,
                    "0.02973"
                  ],
                  [
                    32000,
                    "0.02895"
                  ],
                  [
                    48000,
                    "0.02444"
                  ],
                  [
                    80000,
                    "0.02200"
                  ]
                ]
              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "1246838",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T14:39:45Z",
              "order_multiple": null,
              "in_stock_quantity": 8100,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "GB",
                "has_ecommerce": true,
                "name": "RS Components",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.rs-components.com",
                "id": "3261",
                "uid": "fbaa3ea0de71286d"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=01dc8df&sid=10022&ppid=24403092&vpid=277797924&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "be8d08654390ea0f5a9467e1ff79c921",
              "factory_lead_days": null,
              "prices": {

              },
              "is_authorized": true,
              "is_realtime": false
            },
            {
              "sku": "RUM001L02T2CL",
              "packaging": null,
              "on_order_eta": null,
              "last_updated": "2017-03-14T19:12:09Z",
              "order_multiple": null,
              "in_stock_quantity": 3434,
              "eligible_region": "",
              "moq": null,
              "on_order_quantity": null,
              "octopart_rfq_url": null,
              "__class__": "PartOffer",
              "seller": {
                "display_flag": "US",
                "has_ecommerce": true,
                "name": "Quest",
                "__class__": "Seller",
                "homepage_url": "http:\/\/www.questcomp.com",
                "id": "2412",
                "uid": "b29977939293615e"
              },
              "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0c8f42d&sid=2412&ppid=24403092&vpid=237424745&ct=offers",
              "factory_order_multiple": null,
              "_naive_id": "69551c6692ea6ff32ee603a4cd9fd4f1",
              "factory_lead_days": null,
              "prices": {
                "USD": [
                  [
                    1,
                    "0.15000"
                  ],
                  [
                    34,
                    "0.12000"
                  ],
                  [
                    84,
                    "0.07500"
                  ],
                  [
                    668,
                    "0.05400"
                  ]
                ]
              },
              "is_authorized": false,
              "is_realtime": false
            }
          ],
          "uid": "cdf0058eb4021237",
          "mpn": "RUM001L02T2CL",
          "redirected_uids": [

          ],
          "brand": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Brand",
            "name": "Rohm",
            "uid": "12f2d3f83daac535"
          },
          "octopart_url": "https:\/\/octopart.com\/rum001l02t2cl-rohm-24403092",
          "__class__": "Part",
          "manufacturer": {
            "homepage_url": "http:\/\/www.rohm.com",
            "__class__": "Manufacturer",
            "name": "Rohm",
            "uid": "23ede6e708b5f02a"
          }
        }
      ],
      "hits": 1,
      "__class__": "PartsMatchResult",
      "reference": "RUM001L02T2CL",
      "error": null
    }
  ]
}""")


parts_search_response = json.loads("""{
  "user_currency": "USD",
  "hits": 8,
  "stats_results": {

  },
  "user_country": "US",
  "facet_results": {
    "fields": {

    },
    "queries": {

    }
  },
  "msec": 117,
  "request": {
    "q": "DISTANCE METER, LASER, 100M",
    "start": 0,
    "limit": 10,
    "sortby": "score desc",
    "stats": {

    },
    "filter": {
      "fields": {

      },
      "queries": [

      ]
    },
    "facet": {
      "fields": {

      },
      "queries": [

      ]
    },
    "__class__": "SearchRequest"
  },
  "__class__": "SearchResponse",
  "spec_metadata": {

  },
  "results": [
    {
      "snippet": "Laser Distance Meter +\/- 1mm Accuracy Key Pad Control Vertical\/Horizontal Projection",
      "item": {
        "offers": [
          {
            "sku": "614-1227-ND",
            "packaging": "Bulk",
            "on_order_eta": null,
            "last_updated": "2017-03-12T12:36:54Z",
            "order_multiple": null,
            "in_stock_quantity": 2,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Digi-Key",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.digikey.com",
              "id": "459",
              "uid": "2c3be9310496fffc"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=057d134&sid=459&ppid=23827794&vpid=61927347&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "861509370fbb52c265a77e31716744e6",
            "factory_lead_days": 14,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "FLUKE-424D",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T17:41:31Z",
            "order_multiple": null,
            "in_stock_quantity": 15,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Verical",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.verical.com",
              "id": "2617",
              "uid": "504e954473118389"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0e1cde1&sid=5489&ppid=23827794&vpid=272945727&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "3ac4b69bcc1a5c676db3770bc40c37a1",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "05W4602",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-12T06:09:04Z",
            "order_multiple": null,
            "in_stock_quantity": 13,
            "eligible_region": "US",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newark",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.newark.com",
              "id": "2402",
              "uid": "d294179ef2900153"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=003ea07&sid=2402&ppid=23827794&vpid=52174496&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "51a0b162f235ac3affff478be166face",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "382.50000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "676-FLUKE-424D",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T14:15:32Z",
            "order_multiple": null,
            "in_stock_quantity": 8,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Mouser",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.mouser.com",
              "id": "2401",
              "uid": "a5e060ea85e77627"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=070e0cc&sid=2401&ppid=23827794&vpid=52838226&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "8a8c6b70995527853c501ef8ed7c3862",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ],
                [
                  10,
                  "424.99000"
                ],
                [
                  50,
                  "424.99000"
                ],
                [
                  100,
                  "424.99000"
                ],
                [
                  1000,
                  "424.99000"
                ],
                [
                  10000,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "70230869",
            "packaging": "Bulk",
            "on_order_eta": null,
            "last_updated": "2017-03-11T09:43:37Z",
            "order_multiple": 1,
            "in_stock_quantity": 4,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Allied Electronics",
              "__class__": "Seller",
              "homepage_url": "http:\/\/alliedelec.com",
              "id": "14",
              "uid": "f9e13cebd0892a26"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0db7e41&sid=14&ppid=23827794&vpid=47629328&ct=offers",
            "factory_order_multiple": 1,
            "_naive_id": "90b5e5f12e9156807c601e89db290194",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "09596961357",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T12:02:26Z",
            "order_multiple": null,
            "in_stock_quantity": 0,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Carlton-Bates",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.carltonbates.com",
              "id": "7295",
              "uid": "7043b549455aa384"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0ff3126&sid=18369&ppid=23827794&vpid=88182181&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "568c425c83b823a511c45cb148ef8fad",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "424D",
            "packaging": "Bulk",
            "on_order_eta": "2017-03-18T00:00:00Z",
            "last_updated": "2017-03-12T11:07:09Z",
            "order_multiple": null,
            "in_stock_quantity": 0,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": 1,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Onlinecomponents.com",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.onlinecomponents.com",
              "id": "2429",
              "uid": "e3fd26f7c3e6303a"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=00af06d&sid=2429&ppid=23827794&vpid=58240571&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "3c329d4a2a7409feec6467fe798f7b0c",
            "factory_lead_days": 1,
            "prices": {
              "USD": [
                [
                  1,
                  "382.49000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "EW-97241-16",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-10T12:42:22Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Cole-Parmer",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.coleparmer.com\/",
              "id": "7928",
              "uid": "44128118738c97d5"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=02fbc73&sid=19717&ppid=23827794&vpid=114904221&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "e28714ff3befd73941f5f2016c12b822",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "1692555",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-08T20:42:14Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Walker Industrial",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.walkeremd.com",
              "id": "4599",
              "uid": "cc4e0944f4df1f89"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=02c923e&sid=14294&ppid=23827794&vpid=254526480&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "77f7445d52c29079ac77dd5c6bc8bc76",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "382.49000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "424D",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-02-21T21:32:43Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "US",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Test Equipment Depot",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.fotronic.com",
              "id": "7328",
              "uid": "f05a3550c59c239d"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=00d425b&sid=18462&ppid=23827794&vpid=408631312&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "3e794d592b6f68655408934b70bd0de2",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "382.49000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "11912.W",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-10T09:35:02Z",
            "order_multiple": 1,
            "in_stock_quantity": 0,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "TestEquity",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.testequity.com\/",
              "id": "8704",
              "uid": "58059d0f53638bc2"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=00ca027&sid=21499&ppid=23827794&vpid=195865213&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "657e2f13780c9f287512809d9e5d1d5f",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "658774",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-06T02:20:47Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Crescent Electric Supply Co",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.cesco.com",
              "id": "5842",
              "uid": "6f44aa4e50f0bc83"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=030f21b&sid=16275&ppid=23827794&vpid=114651833&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "c268531a7eebcef64fbf924562f7cab9",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "425.00000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "101774",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T04:13:40Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Conrad",
              "__class__": "Seller",
              "homepage_url": "http:\/\/conrad.com",
              "id": "4782",
              "uid": "7914bc1e42dcaad3"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0f7c592&sid=14587&ppid=23827794&vpid=410886304&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "c12ff4d4c17b8eef9bf704a7d7b58151",
            "factory_lead_days": null,
            "prices": {

            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "FLUKE-424D",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-12T02:07:37Z",
            "order_multiple": null,
            "in_stock_quantity": 7,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "EU",
              "has_ecommerce": true,
              "name": "Distrelec",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.distrelec.com",
              "id": "4617",
              "uid": "e53d2037de5236fa"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=07acba4&sid=14389&ppid=23827794&vpid=109457944&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "1e0f298dcea5424cde71f5b97059879e",
            "factory_lead_days": null,
            "prices": {
              "EUR": [
                [
                  1,
                  "359.00000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "2249956",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-12T06:06:40Z",
            "order_multiple": null,
            "in_stock_quantity": 0,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "GB",
              "has_ecommerce": true,
              "name": "Farnell",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.farnell.com\/",
              "id": "819",
              "uid": "58989d9272cd8b5f"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0f902c7&sid=819&ppid=23827794&vpid=240077889&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "3e9e614fce1c8c29eb28bc30e246e1e8",
            "factory_lead_days": null,
            "prices": {
              "GBP": [
                [
                  1,
                  "326.00000"
                ],
                [
                  3,
                  "309.70000"
                ],
                [
                  5,
                  "293.40000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "2249956",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-12T08:37:03Z",
            "order_multiple": null,
            "in_stock_quantity": 0,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "SG",
              "has_ecommerce": true,
              "name": "element14 APAC",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.element14.com\/",
              "id": "3702",
              "uid": "7f61ba6b5871aca6"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=00fe452&sid=11744&ppid=23827794&vpid=240057575&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "b679619a6d821c34966ff6f45ec4c0da",
            "factory_lead_days": null,
            "prices": {
              "SGD": [
                [
                  1,
                  "739.00000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "7649633",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-02-28T12:06:30Z",
            "order_multiple": null,
            "in_stock_quantity": 31,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "GB",
              "has_ecommerce": true,
              "name": "RS Components",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.rs-components.com",
              "id": "3261",
              "uid": "fbaa3ea0de71286d"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=04a6333&sid=10022&ppid=23827794&vpid=180978641&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "2459ee4d41eafd349fe849ccc7de76b6",
            "factory_lead_days": null,
            "prices": {

            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "424D",
            "packaging": null,
            "on_order_eta": "2017-03-18T00:00:00Z",
            "last_updated": "2017-03-12T08:32:09Z",
            "order_multiple": null,
            "in_stock_quantity": 0,
            "eligible_region": "",
            "moq": 1,
            "on_order_quantity": 1,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "CA",
              "has_ecommerce": true,
              "name": "Electro Sonic",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.e-sonic.com\/",
              "id": "4042",
              "uid": "3405f10f12a9e7c2"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0127baa&sid=13420&ppid=23827794&vpid=131643897&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "aa020d358bc2c4ee5755692d343bf56b",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "405.43940"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          },
          {
            "sku": "FLUKE-424D",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-12T12:29:28Z",
            "order_multiple": null,
            "in_stock_quantity": 0,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Markertek",
              "__class__": "Seller",
              "homepage_url": "http:\/\/www.markertek.com\/",
              "id": "5658",
              "uid": "32b6f7bc0dcae171"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0395491&sid=16030&ppid=23827794&vpid=179849983&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "60d9d42e13d81ed35d81d499f6820e92",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "424.99000"
                ]
              ]
            },
            "is_authorized": false,
            "is_realtime": false
          }
        ],
        "uid": "eddc25bd5de8321b",
        "mpn": "FLUKE-424D",
        "redirected_uids": [
          "02afc8ea3f09dd68",
          "7c4eb43875f0a389",
          "57649f3a221d88a3"
        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "Fluke",
          "uid": "78cfb9c55526af08"
        },
        "octopart_url": "https:\/\/octopart.com\/fluke-424d-fluke-23827794",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "Fluke",
          "uid": "94e351e9bd0a4724"
        }
      },
      "__class__": "SearchResult"
    },
    {
      "snippet": "Mini 100M Handheld Digital Laser Distance Meter Range Finder Diastimeter",
      "item": {
        "offers": [
          {
            "sku": "9SIV0MB54S9927",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T03:25:48Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newegg Business",
              "__class__": "Seller",
              "homepage_url": "https:\/\/www.neweggbusiness.com\/",
              "id": "11168",
              "uid": "d546104cd7800681"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0883796&sid=27355&ppid=80304922&vpid=416017931&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "b75781148f1a7b5df6e064a1f68b5d3e",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "45.38000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          }
        ],
        "uid": "6fc4a20711b8b003",
        "mpn": "ZH74500#",
        "redirected_uids": [

        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "YKS",
          "uid": "e787268de6393040"
        },
        "octopart_url": "https:\/\/octopart.com\/zh74500%23-yks-80304922",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "YKS",
          "uid": "188edd841d30cb49"
        }
      },
      "__class__": "SearchResult"
    },
    {
      "snippet": "100m Mini Digital Laser Distance Meter Range Finder Measure Diastimeter",
      "item": {
        "offers": [
          {
            "sku": "9SIV0KY3K16255",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T03:25:48Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newegg Business",
              "__class__": "Seller",
              "homepage_url": "https:\/\/www.neweggbusiness.com\/",
              "id": "11168",
              "uid": "d546104cd7800681"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=01be6fa&sid=27355&ppid=80304914&vpid=416017918&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "5f002ff1006d01ea51d2039276b049e3",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "50.49000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          }
        ],
        "uid": "2874e5b75600f7b3",
        "mpn": "ZH74400",
        "redirected_uids": [

        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "YKS",
          "uid": "e787268de6393040"
        },
        "octopart_url": "https:\/\/octopart.com\/zh74400-yks-80304914",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "YKS",
          "uid": "188edd841d30cb49"
        }
      },
      "__class__": "SearchResult"
    },
    {
      "snippet": "Mini 100M Handheld Digital Laser Distance Meter Range Finder Diastimeter",
      "item": {
        "offers": [
          {
            "sku": "9SIV0KY3K16042",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T03:25:48Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newegg Business",
              "__class__": "Seller",
              "homepage_url": "https:\/\/www.neweggbusiness.com\/",
              "id": "11168",
              "uid": "d546104cd7800681"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0db5953&sid=27355&ppid=80304921&vpid=416017930&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "903cbe872c5b8c0362d1e6fe1a9bb3bd",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "49.49000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          }
        ],
        "uid": "e2222fe19c5d3de5",
        "mpn": "ZH74500",
        "redirected_uids": [

        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "YKS",
          "uid": "e787268de6393040"
        },
        "octopart_url": "https:\/\/octopart.com\/zh74500-yks-80304921",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "YKS",
          "uid": "188edd841d30cb49"
        }
      },
      "__class__": "SearchResult"
    },
    {
      "snippet": "100m Mini Digital Laser Distance Meter Range Finder Measure Diastimeter",
      "item": {
        "offers": [
          {
            "sku": "9SIV0MB54S9356",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T03:25:48Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newegg Business",
              "__class__": "Seller",
              "homepage_url": "https:\/\/www.neweggbusiness.com\/",
              "id": "11168",
              "uid": "d546104cd7800681"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=069d424&sid=27355&ppid=80304915&vpid=416017919&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "a066c88ccc1aa1f1fc8cccca38fc9e28",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "46.08000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          }
        ],
        "uid": "4dc5800633b09202",
        "mpn": "ZH74400#",
        "redirected_uids": [

        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "YKS",
          "uid": "e787268de6393040"
        },
        "octopart_url": "https:\/\/octopart.com\/zh74400%23-yks-80304915",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "YKS",
          "uid": "188edd841d30cb49"
        }
      },
      "__class__": "SearchResult"
    },
    {
      "snippet": "328ft 100M Handheld Digital Laser Distance Meter Rangefinder Red with Tripod",
      "item": {
        "offers": [
          {
            "sku": "9SIV0KK5359028",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T03:25:48Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newegg Business",
              "__class__": "Seller",
              "homepage_url": "https:\/\/www.neweggbusiness.com\/",
              "id": "11168",
              "uid": "d546104cd7800681"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=0fbb989&sid=27355&ppid=80136005&vpid=415832401&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "65ad47fff7a47e98fb9a5ba6d4d61340",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "59.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          }
        ],
        "uid": "9d2050ec7f0342e7",
        "mpn": "A16011500UX0517",
        "redirected_uids": [

        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "Unique Bargains",
          "uid": "8487458d85355340"
        },
        "octopart_url": "https:\/\/octopart.com\/a16011500ux0517-unique+bargains-80136005",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "Unique Bargains",
          "uid": "ad496843a8fb7e8e"
        }
      },
      "__class__": "SearchResult"
    },
    {
      "snippet": "328ft 100M Digital Laser Distance Meter Measure Rangefinder Yellow w Tripod",
      "item": {
        "offers": [
          {
            "sku": "9SIV0KK5372566",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T03:25:48Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newegg Business",
              "__class__": "Seller",
              "homepage_url": "https:\/\/www.neweggbusiness.com\/",
              "id": "11168",
              "uid": "d546104cd7800681"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=067db09&sid=27355&ppid=80136009&vpid=415832405&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "f7c46797c40519848e02f481754f3e10",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "59.99000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          }
        ],
        "uid": "1611dbddf43ec9d6",
        "mpn": "A16011500UX0521",
        "redirected_uids": [

        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "Unique Bargains",
          "uid": "8487458d85355340"
        },
        "octopart_url": "https:\/\/octopart.com\/a16011500ux0521-unique+bargains-80136009",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "Unique Bargains",
          "uid": "ad496843a8fb7e8e"
        }
      },
      "__class__": "SearchResult"
    },
    {
      "snippet": "100m(328ft) Digital Laser Distance Meter Measure Range Finder Area Volume",
      "item": {
        "offers": [
          {
            "sku": "9SIV0KY3K14879",
            "packaging": null,
            "on_order_eta": null,
            "last_updated": "2017-03-11T03:25:48Z",
            "order_multiple": null,
            "in_stock_quantity": -2,
            "eligible_region": "",
            "moq": null,
            "on_order_quantity": null,
            "octopart_rfq_url": null,
            "__class__": "PartOffer",
            "seller": {
              "display_flag": "US",
              "has_ecommerce": true,
              "name": "Newegg Business",
              "__class__": "Seller",
              "homepage_url": "https:\/\/www.neweggbusiness.com\/",
              "id": "11168",
              "uid": "d546104cd7800681"
            },
            "product_url": "https:\/\/octopart.com\/click\/track?country=US&ak=a8cfd5a0&sig=09e84c5&sid=27355&ppid=80297422&vpid=416009764&ct=offers",
            "factory_order_multiple": null,
            "_naive_id": "d99dd5aaa6b878829348ce3bcd42ea42",
            "factory_lead_days": null,
            "prices": {
              "USD": [
                [
                  1,
                  "59.09000"
                ]
              ]
            },
            "is_authorized": true,
            "is_realtime": false
          }
        ],
        "uid": "d6e01b23ce480927",
        "mpn": "ZC22500",
        "redirected_uids": [

        ],
        "brand": {
          "homepage_url": null,
          "__class__": "Brand",
          "name": "YKS",
          "uid": "e787268de6393040"
        },
        "octopart_url": "https:\/\/octopart.com\/zc22500-yks-80297422",
        "__class__": "Part",
        "manufacturer": {
          "homepage_url": null,
          "__class__": "Manufacturer",
          "name": "YKS",
          "uid": "188edd841d30cb49"
        }
      },
      "__class__": "SearchResult"
    }
  ]
}""")

parts_part_response = json.loads("""{
  "__class__": "Part",
  "brand": {
    "__class__": "Brand",
    "homepage_url": null,
    "name": "Fluke",
    "uid": "78cfb9c55526af08"
  },
  "datasheets": [
    {
      "__class__": "Datasheet",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "element14 APAC",
            "uid": "58989d9272cd8b5f"
          }
        ]
      },
      "metadata": {
        "date_created": "2012-05-15T17:51:59Z",
        "last_updated": "2012-05-15T17:52:22Z",
        "num_pages": 2,
        "size_bytes": 630915
      },
      "mimetype": "application/pdf",
      "url": "http://datasheet.octopart.com/FLUKE-424D-Fluke-datasheet-12564773.pdf"
    },
    {
      "__class__": "Datasheet",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Farnell",
            "uid": "58989d9272cd8b5f"
          }
        ]
      },
      "metadata": {
        "date_created": "2012-07-25T07:52:26Z",
        "last_updated": "2012-07-25T07:52:27Z",
        "num_pages": 2,
        "size_bytes": 137267
      },
      "mimetype": "application/pdf",
      "url": "http://datasheet.octopart.com/FLUKE-424D-Fluke-datasheet-12560617.pdf"
    },
    {
      "__class__": "Datasheet",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Farnell",
            "uid": "58989d9272cd8b5f"
          }
        ]
      },
      "metadata": {
        "date_created": "2012-07-25T07:51:55Z",
        "last_updated": "2012-07-25T07:51:58Z",
        "num_pages": 2,
        "size_bytes": 201939
      },
      "mimetype": "application/pdf",
      "url": "http://datasheet.octopart.com/FLUKE-424D-Fluke-datasheet-12568420.pdf"
    },
    {
      "__class__": "Datasheet",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Farnell",
            "uid": "58989d9272cd8b5f"
          }
        ]
      },
      "metadata": {
        "date_created": "2012-07-25T07:51:14Z",
        "last_updated": "2012-07-25T07:51:17Z",
        "num_pages": 2,
        "size_bytes": 196234
      },
      "mimetype": "application/pdf",
      "url": "http://datasheet.octopart.com/FLUKE-424D-Fluke-datasheet-12564825.pdf"
    },
    {
      "__class__": "Datasheet",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Jameco",
            "uid": "bab57fbf9ab96972"
          }
        ]
      },
      "metadata": {
        "date_created": "2012-05-15T17:49:51Z",
        "last_updated": "2013-01-28T21:00:05Z",
        "num_pages": 2,
        "size_bytes": 174565
      },
      "mimetype": "application/pdf",
      "url": "http://datasheet.octopart.com/FLUKE-424D-Fluke-datasheet-13719724.pdf"
    },
    {
      "__class__": "Datasheet",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Allied Electronics & Automation",
            "uid": "f9e13cebd0892a26"
          }
        ]
      },
      "metadata": {
        "date_created": "2012-04-04T20:24:07Z",
        "last_updated": "2012-04-25T19:10:35Z",
        "num_pages": 2,
        "size_bytes": 522055
      },
      "mimetype": "application/pdf",
      "url": "http://datasheet.octopart.com/424D-Fluke-datasheet-10925636.pdf"
    },
    {
      "__class__": "Datasheet",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Allied Electronics & Automation",
            "uid": "f9e13cebd0892a26"
          }
        ]
      },
      "metadata": {
        "date_created": "2012-05-15T17:51:59Z",
        "last_updated": "2012-07-12T14:15:04Z",
        "num_pages": 2,
        "size_bytes": 625698
      },
      "mimetype": "application/pdf",
      "url": "http://datasheet.octopart.com/424D-Fluke-datasheet-37499250.pdf"
    }
  ],
  "manufacturer": {
    "__class__": "Manufacturer",
    "homepage_url": null,
    "name": "Fluke",
    "uid": "94e351e9bd0a4724"
  },
  "mpn": "FLUKE-424D",
  "octopart_url": "https://octopart.com/fluke-424d-fluke-23827794",
  "offers": [
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "459_614-1227-ND",
      "eligible_region": "",
      "factory_lead_days": 14,
      "factory_order_multiple": null,
      "in_stock_quantity": 1,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T12:46:51Z",
      "moq": 1,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": "Bulk",
      "prices": {
        "USD": [
          [
            1,
            "429.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=057d134&sid=459&ppid=23827794&vpid=61927347&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.digikey.com",
        "id": "459",
        "name": "Digi-Key",
        "uid": "2c3be9310496fffc"
      },
      "sku": "614-1227-ND"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "819_2249956_NL",
      "eligible_region": "NL",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 3,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T13:57:11Z",
      "moq": 1,
      "multipack_quantity": "1",
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "EUR": [
          [
            1,
            "370.00000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=0282c3d&sid=819&ppid=23827794&vpid=240170935&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "GB",
        "has_ecommerce": true,
        "homepage_url": "http://www.farnell.com/",
        "id": "819",
        "name": "Farnell",
        "uid": "58989d9272cd8b5f"
      },
      "sku": "2249956"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "3261_7649633",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 37,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T13:02:52Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {},
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=04a6333&sid=10022&ppid=23827794&vpid=180978641&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "GB",
        "has_ecommerce": true,
        "homepage_url": "http://www.rs-components.com",
        "id": "3261",
        "name": "RS Components",
        "uid": "fbaa3ea0de71286d"
      },
      "sku": "7649633"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "2401_676-FLUKE-424D",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 6,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T03:01:06Z",
      "moq": 1,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "429.99000"
          ],
          [
            10,
            "429.99000"
          ],
          [
            50,
            "429.99000"
          ],
          [
            100,
            "429.99000"
          ],
          [
            1000,
            "429.99000"
          ],
          [
            10000,
            "429.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=070e0cc&sid=2401&ppid=23827794&vpid=52838226&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.mouser.com",
        "id": "2401",
        "name": "Mouser",
        "uid": "a5e060ea85e77627"
      },
      "sku": "676-FLUKE-424D"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "4599_1692555",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 4,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-09-21T20:36:14Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "429.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=02c923e&sid=14294&ppid=23827794&vpid=254526480&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.walkeremd.com",
        "id": "4599",
        "name": "Walker Industrial",
        "uid": "cc4e0944f4df1f89"
      },
      "sku": "1692555"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "10434_166312015",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": -2,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T00:20:06Z",
      "moq": 1,
      "multipack_quantity": "1",
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": 1,
      "packaging": null,
      "prices": {
        "CAD": [
          [
            1,
            "557.97000"
          ]
        ],
        "EUR": [
          [
            1,
            "366.30000"
          ]
        ],
        "USD": [
          [
            1,
            "429.34000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=064d2d8&sid=26605&ppid=23827794&vpid=217729152&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "EU",
        "has_ecommerce": true,
        "homepage_url": "https://www.omnical.nl/",
        "id": "10434",
        "name": "Omnical",
        "uid": "8c0849028dac5fcf"
      },
      "sku": "166312015"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "4782_101774",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 2,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T02:09:18Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "EUR": [
          [
            1,
            "325.00000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=0f7c592&sid=14587&ppid=23827794&vpid=410886304&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "DE",
        "has_ecommerce": true,
        "homepage_url": "http://conrad.com",
        "id": "4782",
        "name": "Conrad",
        "uid": "7914bc1e42dcaad3"
      },
      "sku": "101774"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "7928_EW-97241-16",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": -3,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T11:55:19Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "386.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=02fbc73&sid=19717&ppid=23827794&vpid=114904221&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.coleparmer.com/",
        "id": "7928",
        "name": "Cole-Parmer",
        "uid": "44128118738c97d5"
      },
      "sku": "EW-97241-16"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "2591_424D",
      "eligible_region": "",
      "factory_lead_days": 9,
      "factory_order_multiple": null,
      "in_stock_quantity": 0,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T08:41:30Z",
      "moq": 1,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": "2018-10-25T00:00:00Z",
      "on_order_quantity": 1,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "429.99000"
          ],
          [
            3,
            "408.49000"
          ],
          [
            5,
            "386.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=04e4fbf&sid=2595&ppid=23827794&vpid=58240324&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://masterdistributors.com/",
        "id": "2591",
        "name": "Master Electronics",
        "uid": "2f93ea990ceafc54"
      },
      "sku": "424D"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "2429_424D",
      "eligible_region": "",
      "factory_lead_days": 9,
      "factory_order_multiple": null,
      "in_stock_quantity": 0,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T11:02:51Z",
      "moq": 1,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": "2018-10-25T00:00:00Z",
      "on_order_quantity": 1,
      "order_multiple": null,
      "packaging": "Bulk",
      "prices": {
        "USD": [
          [
            1,
            "429.99000"
          ],
          [
            3,
            "408.49000"
          ],
          [
            5,
            "386.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?c=1&ak=69ec4b8e&sig=0a31102&sid=2429&ppid=23827794&vpid=58240571&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.onlinecomponents.com",
        "id": "2429",
        "name": "Onlinecomponents.com",
        "uid": "e3fd26f7c3e6303a"
      },
      "sku": "424D"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "2426_FLUKE-424D",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 1,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T13:28:06Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {},
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=052ac25&sid=2426&ppid=23827794&vpid=217152896&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.ralphselectronics.com",
        "id": "2426",
        "name": "Ralph's Industrial Electronics",
        "uid": "a737623d872b74f0"
      },
      "sku": "FLUKE-424D"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "2402_05W4602_US",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 9,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T05:41:18Z",
      "moq": 1,
      "multipack_quantity": "1",
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "387.00000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=003ea07&sid=2402&ppid=23827794&vpid=52174496&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.newark.com",
        "id": "2402",
        "name": "Newark",
        "uid": "d294179ef2900153"
      },
      "sku": "05W4602"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "14_70230869",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": 1,
      "in_stock_quantity": 5,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T09:46:14Z",
      "moq": 1,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": 1,
      "packaging": "Bulk",
      "prices": {
        "USD": [
          [
            1,
            "429.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=0db7e41&sid=14&ppid=23827794&vpid=47629328&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://alliedelec.com",
        "id": "14",
        "name": "Allied Electronics & Automation",
        "uid": "f9e13cebd0892a26"
      },
      "sku": "70230869"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "7328_424D_US",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 10,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T06:38:24Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "386.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=00d425b&sid=18462&ppid=23827794&vpid=408631312&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.fotronic.com",
        "id": "7328",
        "name": "Test Equipment Depot",
        "uid": "f05a3550c59c239d"
      },
      "sku": "424D"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "3702_2249956_SG",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 1,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T08:34:41Z",
      "moq": 1,
      "multipack_quantity": "1",
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "SGD": [
          [
            1,
            "728.00000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=00fe452&sid=11744&ppid=23827794&vpid=240057575&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "SG",
        "has_ecommerce": true,
        "homepage_url": "http://www.element14.com/",
        "id": "3702",
        "name": "element14 APAC",
        "uid": "7f61ba6b5871aca6"
      },
      "sku": "2249956"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "4617_18075759_NL",
      "eligible_region": "NL",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 4,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T13:39:32Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {},
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=0b4cd18&sid=14389&ppid=23827794&vpid=468992219&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "EU",
        "has_ecommerce": true,
        "homepage_url": "http://www.distrelec.com",
        "id": "4617",
        "name": "Distrelec",
        "uid": "e53d2037de5236fa"
      },
      "sku": "18075759"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "14_70232958",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": 1,
      "in_stock_quantity": 0,
      "is_authorized": true,
      "is_realtime": false,
      "last_updated": "2018-10-10T09:46:14Z",
      "moq": 1,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": 1,
      "packaging": "Bulk",
      "prices": {
        "USD": [
          [
            1,
            "375.00000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?c=1&ak=69ec4b8e&sig=0e18162&sid=14&ppid=23827794&vpid=48691462&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://alliedelec.com",
        "id": "14",
        "name": "Allied Electronics & Automation",
        "uid": "f9e13cebd0892a26"
      },
      "sku": "70232958"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "1532_FLK-424D",
      "eligible_region": "",
      "factory_lead_days": 35,
      "factory_order_multiple": null,
      "in_stock_quantity": 3,
      "is_authorized": false,
      "is_realtime": false,
      "last_updated": "2018-10-10T00:08:43Z",
      "moq": 1,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": 1,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "415.35000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=05f176c&sid=1532&ppid=23827794&vpid=187748027&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "PL",
        "has_ecommerce": true,
        "homepage_url": "http://www.tme.eu/en/",
        "id": "1532",
        "name": "TME",
        "uid": "223ee7340ea4f1f9"
      },
      "sku": "FLK-424D"
    },
    {
      "__class__": "PartOffer",
      "_custom": {},
      "_naive_id": "5658_FLUKE-424D",
      "eligible_region": "",
      "factory_lead_days": null,
      "factory_order_multiple": null,
      "in_stock_quantity": 0,
      "is_authorized": false,
      "is_realtime": false,
      "last_updated": "2018-10-10T12:29:52Z",
      "moq": null,
      "multipack_quantity": null,
      "octopart_rfq_url": null,
      "on_order_eta": null,
      "on_order_quantity": null,
      "order_multiple": null,
      "packaging": null,
      "prices": {
        "USD": [
          [
            1,
            "424.99000"
          ]
        ]
      },
      "product_url": "https://octopart.com/click/track?ak=69ec4b8e&sig=0395491&sid=16030&ppid=23827794&vpid=179849983&ct=offers",
      "seller": {
        "__class__": "Seller",
        "display_flag": "US",
        "has_ecommerce": true,
        "homepage_url": "http://www.markertek.com/",
        "id": "5658",
        "name": "Markertek",
        "uid": "32b6f7bc0dcae171"
      },
      "sku": "FLUKE-424D"
    }
  ],
  "redirected_uids": [
    "02afc8ea3f09dd68",
    "57649f3a221d88a3",
    "7c4eb43875f0a389"
  ],
  "short_description": "Fluke Laser Distance Meter Includes Compass and Pouch 80 Meters 260 Feet",
  "specs": {
    "packaging": {
      "__class__": "SpecValue",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Ciiva",
            "uid": "8c5c4956cfa65f9b"
          }
        ]
      },
      "display_value": "Bulk",
      "max_value": null,
      "metadata": {
        "__class__": "SpecMetadata",
        "datatype": "string",
        "key": "packaging",
        "name": "Packaging",
        "unit": null
      },
      "min_value": null,
      "value": [
        "Bulk"
      ]
    },
    "reach_svhc_compliance": {
      "__class__": "SpecValue",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Farnell",
            "uid": "58989d9272cd8b5f"
          }
        ]
      },
      "display_value": "No SVHC",
      "max_value": null,
      "metadata": {
        "__class__": "SpecMetadata",
        "datatype": "string",
        "key": "reach_svhc_compliance",
        "name": "REACH SVHC Compliance",
        "unit": null
      },
      "min_value": null,
      "value": [
        "No SVHC"
      ]
    },
    "rohs_status": {
      "__class__": "SpecValue",
      "attribution": {
        "__class__": "Attribution",
        "first_acquired": null,
        "sources": [
          {
            "__class__": "Source",
            "name": "Farnell",
            "uid": "58989d9272cd8b5f"
          }
        ]
      },
      "display_value": "Not Applicable",
      "max_value": null,
      "metadata": {
        "__class__": "SpecMetadata",
        "datatype": "string",
        "key": "rohs_status",
        "name": "RoHS",
        "unit": null
      },
      "min_value": null,
      "value": [
        "Not Applicable"
      ]
    }
  },
  "uid": "eddc25bd5de8321b"
}""")