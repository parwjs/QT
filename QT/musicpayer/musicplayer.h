#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QFileDialog>
#include <QString>
#include <QMediaPlayer>
#include <QFileInfo>
#include <QMessageBox>
#include <QListWidget>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    QMediaPlayer *myplayer = new QMediaPlayer;
    int voicenum=80;
    int flag=0;

private slots:
    void on_play_clicked();

    void on_pause_clicked();

    void on_song_bar_sliderMoved(int position);

    void on_clear_clicked();

    void changea(qint64 position);

    void on_voice_bar_sliderMoved(int position);

    void on_open_clicked();

    void on_song_list_itemDoubleClicked(QListWidgetItem *item);

    void on_list_clicked();

    void on_front_clicked();

    void on_next_clicked();

    void on_song_list_itemClicked(QListWidgetItem *item);

private:
    Ui::MainWindow *ui;


};

#endif // MAINWINDOW_H
