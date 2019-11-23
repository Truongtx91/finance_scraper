# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

class StockTwPipeline(object):
    def process_item(self, item, spider):
        return item

class NdxPipeline(object):

    def open_spider(self, spider):
        
        self.file       = open("NDX_5Y.csv", "wb")
        self.exporter   = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):

        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):

        self.exporter.finish_exporting()
        self.file.close()