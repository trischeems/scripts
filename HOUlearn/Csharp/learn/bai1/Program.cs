using System;
using System.Runtime.InteropServices;

class Program
{
    static void Main()
    {
        //string a, b;
        //Console.Write("Nhap so a : ");
        //a = Console.ReadLine();
        //int soA = Int32.Parse(a);
        //Console.Write("Nhap so b: ");
        //b = Console.ReadLine();
        //int soB = Int32.Parse(b);
        //string kq = (soA > soB) ? "So a to hon" : "so b to hon";
        //Console.WriteLine("{0}", kq);
        //Console.ReadKey();

        //int muc1 = 1678;
        //int muc2 = 1734;
        //int muc3 = 2014;
        //int muc4 = 2927;
        //string kwhR;
        //int tt = 0;
        //kwhR = Console.ReadLine();
        //int kwh = Int32.Parse(kwhR);

        //if(kwh <= 100)
        //{
        //    tt = kwh*muc1;
        //}else if(kwh <= 200 && kwh > 100)
        //{
        //    tt = (100 * muc1) + ((kwh - 100) * muc2);
        //}else if(kwh <= 300 && kwh > 200)
        //{
        //    tt = (100 * muc1) + (100 * muc2) + ((kwh - 100) * muc3);
        //}else if(kwh > 300)
        //{
        //    tt = (100 * muc1) + (100 * muc2) + (100 * muc3) + ((kwh - 100) * muc4);
        //}
        //Console.Write("So tien dien thang nay : " + tt);
        //Console.ReadKey();

        //Console.Write("Nhap nam : ");
        //int year = Int32.Parse(Console.ReadLine());
        //Console.Write("Nhap thang : ");
        //int month = Int32.Parse(Console.ReadLine());

        //bool isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        //int daysInMonth;
        //switch (month)
        //{
        //    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
        //        daysInMonth = 31;
        //        break;
        //    case 4: case 6: case 9: case 11:
        //        daysInMonth = 30;
        //        break;
        //    case 2:
        //        daysInMonth = isLeapYear ? 29 : 28;
        //        break;
        //    default:
        //        Console.WriteLine("Thang khong hop le !");
        //        return;
        //}
        //Console.WriteLine("Thang : " + month + " nam " + year + " co " + daysInMonth + " ngay !");
        //Console.ReadKey();

        string giaTri = "oke";
        int i = 0;
        //for(int i = 0; i < 10; i++)
        //{
        //    Console.WriteLine(giaTri);
        //}

        do
        {
            Console.WriteLine(giaTri);
            i++;
        } while (i < 10);

        Console.ReadLine();


    }
}
