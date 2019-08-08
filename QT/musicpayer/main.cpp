#include "musicplayer.h"
#include <QApplication>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setWindowTitle("musicplayer");
    w.setMinimumSize(720,582);
    w.setMaximumSize(720,582);
    w.setAutoFillBackground(true);
    QPalette palette = w.palette();
    palette.setBrush(QPalette::Window,QBrush(QPixmap(":/Images/2.jpg").scaled(w.size(),Qt::IgnoreAspectRatio,Qt::SmoothTransformation)));
    w.setPalette(palette);
    w.show();

    return a.exec();
}
