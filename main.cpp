#include <QApplication>
#include <QtWidgets>
#include "qfonticon.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QFontIcon::addFont(":/fa-solid-900.ttf");
    QFontIcon::addIconNames(":/solid-names.json");

    QGridLayout * iconsLayout = new QGridLayout;
    QWidget * iconsWidget = new QWidget;
    iconsWidget->setWindowTitle("Some icons from awesome font");
    iconsWidget->setLayout(iconsLayout);

    QList<QString> names = QFontIcon::allNames();

    for (int x=0; x<10; x++)
    {
        for (int y=0;y<10; y++)
        {
	    QString name = names.value(x*10 + y);
            QPushButton * button = new QPushButton(QFontIcon::icon(name), name);
            iconsLayout->addWidget(button,x,y);
            if (y == 5)
                button->setDisabled(true);
        }
    }

    iconsWidget->show();

    return a.exec();
}
