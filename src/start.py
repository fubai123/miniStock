from src.qtsrc.index import *

if __name__ == '__main__':
    # 实例化表格
    app = QApplication(sys.argv)
    myTable = MyTable()

    # 启动更新线程
    stock_url = 'http://hq.sinajs.cn/list='
    update_data_thread = UpdateData(GetStockData(stock_url), code='600519')
    update_data_thread.update_date.connect(myTable.update_item_data)  # 链接信号
    update_data_thread.start()

    # 显示在屏幕中央
    desktop = QApplication.desktop()  # 获取坐标
    x = (desktop.width() - myTable.width()) // 2
    y = (desktop.height() - myTable.height()) // 2
    myTable.move(x, y)  # 移动

    # 显示表格
    myTable.show()
    app.exit(app.exec_())