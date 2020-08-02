#include "widget.h"
#include "ui_widget.h"
#include <QMessageBox>
#include <stdlib.h>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_pushButton_clicked()
{
    //QMessageBox::information(this, "标题", "hello world");
    system("calc");
}

void Widget::on_pushButton_2_clicked()
{
    int a;
    a = ui->lineEdit->text().toInt();//把用户在输入框中输入的字符串转化为整数
    int b;
    b = ui->lineEdit_2->text().toInt();
    int c;
    c = a + b;
    //QString::number(c)把变量c转化成一个字符串
    QMessageBox::information(this, "计算结果", QString::number(c));
}
