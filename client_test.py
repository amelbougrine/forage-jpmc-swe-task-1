import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Call getDataPoint with the first quote
        stock1, bid_price1, ask_price1, price1 = getDataPoint(quotes[0])

        # Assert if the returned values match the expected values
        self.assertEqual(stock1, 'ABC')
        self.assertAlmostEqual(bid_price1, 120.48)
        self.assertAlmostEqual(ask_price1, 121.2)
        self.assertAlmostEqual(price1, (120.48 + 121.2) / 2)

        # Call getDataPoint with the second quote
        stock2, bid_price2, ask_price2, price2 = getDataPoint(quotes[1])

        # Assert if the returned values match the expected values
        self.assertEqual(stock2, 'DEF')
        self.assertAlmostEqual(bid_price2, 117.87)
        self.assertAlmostEqual(ask_price2, 121.68)
        self.assertAlmostEqual(price2, (117.87 + 121.68) / 2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Call getDataPoint with the first quote
        stock1, bid_price1, ask_price1, price1 = getDataPoint(quotes[0])

        # Assert if the returned values match the expected values
        self.assertEqual(stock1, 'ABC')
        self.assertAlmostEqual(bid_price1, 120.48)
        self.assertAlmostEqual(ask_price1, 119.2)
        self.assertAlmostEqual(price1, (120.48 + 119.2) / 2)

        # Call getDataPoint with the second quote
        stock2, bid_price2, ask_price2, price2 = getDataPoint(quotes[1])

        # Assert if the returned values match the expected values
        self.assertEqual(stock2, 'DEF')
        self.assertAlmostEqual(bid_price2, 117.87)
        self.assertAlmostEqual(ask_price2, 121.68)
        self.assertAlmostEqual(price2, (117.87 + 121.68) / 2)

    def test_getRatio_non_zero_prices(self):
        # Arrange: Prepare dummy data for testing
        price_a = 20.0
        price_b = 10.0

        # Act: Call the method with non-zero prices
        ratio = getRatio(price_a, price_b)

        # Assert: Check if the output matches the expected value
        self.assertAlmostEqual(ratio, 2.0)  # 20.0 / 10.0 = 2.0

    def test_getRatio_price_b_zero(self):
        # Arrange: Prepare dummy data for testing
        price_a = 20.0
        price_b = 0.0

        # Act: Call the method with price_b as zero
        ratio = getRatio(price_a, price_b)

        # Assert: Check if the output matches the expected value (None)
        self.assertIsNone(ratio)

    def test_getRatio_price_a_zero(self):
        # Arrange: Prepare dummy data for testing
        price_a = 0.0
        price_b = 10.0

        # Act: Call the method with price_a as zero
        ratio = getRatio(price_a, price_b)

        # Assert: Check if the output matches the expected value (None)
        self.assertIsNone(ratio)

    def test_getRatio_both_prices_zero(self):
        # Arrange: Prepare dummy data for testing
        price_a = 0.0
        price_b = 0.0

        # Act: Call the method with both prices as zero
        ratio = getRatio(price_a, price_b)

        # Assert: Check if the output matches the expected value (None)
        self.assertIsNone(ratio)


if __name__ == '__main__':
    unittest.main()
