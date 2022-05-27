import sys
import RTMP_Server_Conf
import UI.GUI as ui
from PyQt5.QtWidgets import QApplication,QMainWindow
from functools import partial

def run():
    Stream_Name = ui.Stream_Name.text()
    RTMP_Server_Port=ui.RTMP_Server_Port.text()
    Max_Link_Connection=ui.Max_Link_Connection.text()
    Trunk_Block=ui.Trunk_Block.text()
    Status_Port=ui.Status_Port.text()
    result = RTMP_Server_Conf.MAIN(Stream_Name,RTMP_Server_Port,Max_Link_Connection,Trunk_Block,Status_Port)
    ui.RTMP_Address.setText(str(result[0]))
    ui.RTMP_Key.setText(str(result[1]))
    ui.Live_Watch_Address.setText(str(result[2]))
    ui.Server_Status_Address.setText(str(result[3]))
    RTMP_Server_Conf.RUN_CMD(1)

if __name__=='__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.IP_show.setText(str(RTMP_Server_Conf.Get_Host_IP()))

    ui.Run.clicked.connect(run)


    sys.exit(app.exec_())