#include "musicplayer.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_list_clicked()
{
    QStringList songlist = QFileDialog::getOpenFileNames(this,"添加","/","*.mp3");
    ui->song_list->addItems(songlist);
         ui->front->setEnabled(true);
          ui->next->setEnabled(true);
}


void MainWindow::on_song_list_itemDoubleClicked(QListWidgetItem *item)
{
    QString song = ui->song_list->currentItem()->text();
       QFileInfo info(song);
        myplayer->setMedia(QUrl::fromLocalFile(song));
        myplayer->setVolume(voicenum);
        ui->play->setText("||");
        myplayer->play();
        ui->voice_bar->setValue(voicenum);
        connect(myplayer, &QMediaPlayer::positionChanged,this,&MainWindow::changea);
        ui->song_list->currentItem()->setSelected(item);
        ui->song_name->setText(info.baseName());
        ui->addr->setText(info.baseName());
        ui->addr->hide();
        ui->temp_name->setText(song);
        ui->temp_name->hide();
}

void MainWindow::on_front_clicked()
{
    int current_num = ui->song_list->currentRow();
        if (current_num==0){
           int front_num = ui->song_list->count()-1;
           QString front_song = ui->song_list->item(front_num)->text();
           myplayer->stop();
           myplayer->setMedia(QUrl::fromLocalFile(front_song));
           myplayer->setVolume(voicenum);
           ui->voice_bar->setValue(voicenum);
           myplayer->play();
           connect(myplayer, &QMediaPlayer::positionChanged,this,&MainWindow::changea);
           ui->song_list->item(front_num)->setSelected(true);
           ui->song_list->setCurrentRow(front_num);
           QFileInfo info(ui->song_list->item(front_num)->text());
           ui->song_name->setText(info.baseName());
        }

        else {
        int front_num = current_num-1;
        QString front_song = ui->song_list->item(front_num)->text();
        myplayer->stop();
        myplayer->setMedia(QUrl::fromLocalFile(front_song));
        myplayer->setVolume(voicenum);
        ui->voice_bar->setValue(voicenum);
        myplayer->play();
        connect(myplayer, &QMediaPlayer::positionChanged,this,&MainWindow::changea);
        ui->song_list->item(front_num)->setSelected(true);
        ui->song_list->setCurrentRow(front_num);
        QFileInfo info(ui->song_list->item(front_num)->text());
        ui->song_name->setText(info.baseName());
        }
}

void MainWindow::on_next_clicked()
{
    int current_num = ui->song_list->currentRow();
        if (current_num==ui->song_list->count()-1){
           int next_num = 0;
           QString front_song = ui->song_list->item(next_num)->text();
           myplayer->stop();
           myplayer->setMedia(QUrl::fromLocalFile(front_song));
           myplayer->setVolume(voicenum);
           ui->voice_bar->setValue(voicenum);
           myplayer->play();
           connect(myplayer, &QMediaPlayer::positionChanged,this,&MainWindow::changea);
           ui->song_list->item(next_num)->setSelected(true);
           ui->song_list->setCurrentRow(next_num);
           QFileInfo info(ui->song_list->item(next_num)->text());
           ui->song_name->setText(info.baseName());

        }

        else {
        int next_num = current_num+1;
        QString front_song = ui->song_list->item(next_num)->text();
        myplayer->stop();
        myplayer->setMedia(QUrl::fromLocalFile(front_song));
        myplayer->setVolume(voicenum);
        ui->voice_bar->setValue(voicenum);
        myplayer->play();


        connect(myplayer, &QMediaPlayer::positionChanged,this,&MainWindow::changea);
        ui->song_list->item(next_num)->setSelected(true);
        ui->song_list->setCurrentRow(next_num);
        QFileInfo info(ui->song_list->item(next_num)->text());
        ui->song_name->setText(info.baseName());
        }
}

void MainWindow::on_song_list_itemClicked(QListWidgetItem *item)
{
    QString songname = ui->song_list->currentItem()->text();
        ui->temp_name->setText(songname);
        ui->temp_name->hide();
}




void MainWindow::on_pause_clicked()
{
    myplayer->stop();
    ui->play->setText("▶");
}

void MainWindow::on_song_bar_sliderMoved(int position)
{
    qint64 total_time = myplayer->duration();
    myplayer->setPosition(position*1.0/100*total_time);

}


void MainWindow::on_clear_clicked()
{
    if(ui->song_list->count() != 0){
               ui->song_list->currentItem()->setText("");
               int count = ui->song_list->currentRow();
               int so = ui->song_list->count();
               for (int i=count;i<so-1;i++) {
                    ui->song_list->item(i)->setText(ui->song_list->item(i+1)->text());
               }
            QListWidgetItem  *item = ui->song_list->takeItem(so-1);
            ui->song_list->removeItemWidget(item);
            delete item;


        }
}


void MainWindow::on_voice_bar_sliderMoved(int position)
{
    myplayer->setVolume(position);
}

void MainWindow::on_play_clicked()
{
    QString songpath = ui->temp_name->text();
        if (songpath == ""){
            QMessageBox::warning(this,"警告","请打开歌曲!");
        }
        else {
            if (flag == 0){
            myplayer->setMedia(QUrl::fromLocalFile(songpath));
            myplayer->setVolume(voicenum);
            myplayer->play();
            ui->voice_bar->setValue(voicenum);
            QString songname = ui->addr->text();
            ui->song_name->setText(songname);
            connect(myplayer, &QMediaPlayer::positionChanged,this,&MainWindow::changea);

                   flag = 1;
                   }
                   QString now = ui->play->text();
                   if (flag==1){
                       if(now=="▶"){
                           ui->play->setText("||");
                           myplayer->play();
                       }
                       if(now=="||"){
                           ui->play->setText("▶");
                           myplayer->pause();

                       }
                   }

               }
}


void MainWindow::changea(qint64 position){
                qint64 total_time = myplayer->duration();
                int ps = (int)position;
               int show_minite = ps/60000;
               int show_seconds = ps/1000%60;
               QString show_time = QString::number(show_minite)+":"+QString::number(show_seconds);
                ui->now_time->setText(show_time);
                ui->song_bar->setValue(position*1.0/total_time*100);
                if(ui->song_bar->value() == 99){
                    ui->play->setText("▶");
                    ui->voice_bar->setValue(0);
                }
//                qDebug()<<(ui->horizontalSlider_2->value());


                    if(myplayer->duration() != 0)
                    {
                       qint64 time = myplayer->duration();
                       time = int(time);
                       int minite = time/60000;
                       int seconds = time/1000%60;
                      QString durationtime = QString::number(minite)+":"+QString::number(seconds);
                        ui->total_time->setText(durationtime);
                    }

}


void MainWindow::on_open_clicked()
{
    QString filename =  QFileDialog::getOpenFileName(this,"打开","/","*.mp3");
    QFileInfo info(filename);
    QString songname = info.baseName();
    ui->addr->setText(songname);//addr->label2
    ui->addr->hide();
    ui->temp_name->setText(filename);//temp_name->label5
    ui->temp_name->hide();
    if (flag == 1){
        myplayer->stop();
        ui->play->setText("▶");
        myplayer->setMedia(QUrl::fromLocalFile(filename));
        QFileInfo info(filename);
        QString songname = info.baseName();
        ui->song_name->setText(songname);
        myplayer->setVolume(voicenum);
    //      myplayer->play();
    }
    ui->front->setEnabled(false);
       ui->next->setEnabled(false);
}
