//public class Main {
//    public static void main(String[] args) {
////        int sum = 0;
////        int number =1;
////        do{
////            System.out.println(number);
////            sum += number;
////            number +=3;
////        }
////        while(sum <= 200);
//
////        int i=1, t=0;
////        while(true){
////            t=t+i;
////            if(t>200)break;
////            System.out.println(i + " ");
////            i = i+3;
////        }
////    }
//
//
//
//}

//####### ghi du lieu vao tep
//import java.io.FileOutputStream;
//import java.io.PrintStream;
//public class Main{
//    public static void main(String[] arg) throws Exception{
//        PrintStream ps = new PrintStream(new FileOutputStream("minhtri.txt"));
//        ps.print("Pham minh tri");
//        ps.println();
//        ps.printf("%d", 2002);
//        ps.close();
//    }
//}


//####### doc tep va hien du lieu ra man hinh
//import java.io.FileInputStream;
//import java.io.FileOutputStream;
//import java.util.Scanner;
//
//public class Main{
//    public static void main(String[] arg) throws Exception{
//        Scanner sc = new Scanner(new FileInputStream("minhtri.txt"));
//        String ten = sc.nextLine();
//        int nam = sc.nextInt();
//        sc.close();
//        System.out.printf("%s \n %d", ten,nam);
//
//    }
//}


// ############## hien kieu ngay thang ra man hinh
//import java.util.Date;
//
//public class Main {
//    public static void main(String[] args) {
//        Date d = new Date(System.currentTimeMillis());
//        System.out.printf("Hien tai la %1$tH:%1$tM:%1$tS - ngay %1$td/%1$tm/%1$tY", d);
//    }
//}

//// ############# lay ngay thang nam hien tai bang calendar
//import java.text.SimpleDateFormat;
//import java.util.Calendar;
//import java.io.FileOutputStream;
//import java.io.PrintStream;
//import java.util.Date;
//public class Main{
//    public static void main(String[] arg) throws Exception{
//        Calendar cal = Calendar.getInstance();
//        SimpleDateFormat sp = new SimpleDateFormat("dd/MM/yyyy");
//        Date d = new Date(System.currentTimeMillis());
//
//
//        PrintStream p = new PrintStream(new FileOutputStream("date_new.txt"));
//        p.println(("Ngay : " + cal.get(Calendar.DAY_OF_MONTH) + ("\nThang : "+ (cal.get(Calendar.MONTH) +1)) + ("\nNam : " + cal.get(Calendar.YEAR))));
//        p.println(sp.format(cal.getTime()));
//        p.printf("Gio hien tai : %1$tH:%1$tM:%1$tS",d);
//        p.close();
////        System.out.println("Ngay : " + cal.get(Calendar.DAY_OF_MONTH));
////        System.out.println("Thang : " + (cal.get(Calendar.MONTH) +1));
////        System.out.println("Nam : " + cal.get(Calendar.YEAR));
////        System.out.println(sp.format(cal.getTime()));
//
//    }
//}

//// ################# chuyen doi sau ve dang ten rieng
//import java.io.FileOutputStream;
//import java.io.PrintStream;
//import java.text.SimpleDateFormat;
//import java.util.Date;
//import java.util.Calendar;
//
//public class Main{
//    public static void main(String[] arg) throws Exception{
//        // doi xau sang ten rieng
//        String xau = "tri dep trai";
//        String s= "";
//        xau = " " + xau.toLowerCase();
//        for(int i = 0;i<xau.length()-1;i++){
//            if(xau.charAt(i) == ' ' && xau.charAt(i + 1) !=' '){
//                s=s + xau.valueOf(xau.charAt(i+1)).toUpperCase();
//            }
//            else{
//                s=s + xau.charAt(i+1);
//            }
//        }
////        System.out.print(s);
//        // lay gia tri cua ngay gio hien tai
//        Calendar cal = Calendar.getInstance();
//        SimpleDateFormat sp = new SimpleDateFormat("dd/MM/yyyy");
//        Date d = new Date(System.currentTimeMillis());
//        // dua ten nay vao trong file
//        PrintStream ps = new PrintStream(new FileOutputStream("data.txt"));
//        ps.print(s);
//        ps.println(("\nNgay : "+ cal.get(Calendar.DAY_OF_MONTH) + " Thang : " + (cal.get(Calendar.MONTH)) + " Nam : " + cal.get(Calendar.YEAR)));
//        ps.printf("sua lan thu : %d", 3);
//        ps.printf("\n%1$tH:%1$tM:%1$tS",d);
//        ps.close();
//
//    }
//}

//// ######## ramdom cac day so khong trung nhau
//import java.util.Random;
//public class Main{
//    public static void main(String[] arg){
//        int i,n = 100;
//        int a[] = new int [n];
//        Random rd = new Random();
//        for(i=0;i<n;i++){
//            a[i] = rd.nextInt(500)+1;
//            System.out.println(a[i]+" ");
//        }
//    }
//}

////###### xu li ngoai le
//
//import java.util.Random;
//import java.util.Scanner;
//public class Main{
//    public static void main(String[] arg){
//        try{
//            Scanner n = new Scanner(System.in);
//            System.out.print("Nhap xau ky tu: ");
//            String s=n.nextLine();
//            int a = Integer.parseInt(s);
//            System.out.printf("\nKet qua chuyen : %d\n",a);
//        }
//        catch(Exception s){
//            System.out.print("\nWrong number\n");
//        }
//        finally {
//            System.out.print("\nFinally\n");
//        }
//        System.out.print("\nContinue\n");
//    }
//}

//// ####### vi du ve tham chieu this
//class Main{
//    int test = 10;
//    void printTest(){
//        int test = 20;
//        System.out.println("test = "+test);
//    }
//    public static void main(String[] arg){
//        Main a =new Main();
//        a.printTest();
//        System.out.println("test = " + this.test);
//    }
//}

//// ####### xay dung lop hinh tron
//import java.util.Scanner;
//public class Main{
//    double bk;
//    public double dientich(){
//        return bk*bk*Math.PI;
//    }
//    public double chuvi(){
//        return bk*2*Math.PI;
//    }
//    public void nhap(){
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap ban kinh : ");
//        bk = sc.nextDouble();
//    }
//    public static void main(String[] arg){
//        Main ht = new Main();
//        ht.nhap();
//        System.out.printf("\nChu vi : %10.2f", ht.chuvi());
//        System.out.printf("\nDien tich : %10.2f", ht.dientich());
//    }
//}

//// ####### tao va nhap doi tuong sinh vien
//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.io.IOException;
//public class Main{
//    private String hoten;
//    private String ngaysinh;
//    private Boolean gioitinh;
//    public void nhap() throws IOException{
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        System.out.print("Nhap ho ten : ");
//            hoten = br.readLine();
//        System.out.print("Ngay sinh : ");
//            ngaysinh = br.readLine();
//        System.out.print("Gioi tinh (1 -> Nam;2 -> Nu) : ");
//        int gt;
//        try{
//            gt = Integer.parseInt(br.readLine());
//            gioitinh = (gt == 1?true:false);
//        }
//        catch(NumberFormatException e){
//            System.out.print("Vui long nhap 1 hoac 2 cho gioi tinh !");
//            gioitinh = null;
//        }
//
//    }
//    public void hien(){
//        System.out.println("Ho va ten : "+ hoten);
//        System.out.println("Ngay sinh : "+ ngaysinh);
//        System.out.println("Goi tinh : " + (gioitinh == true?"Nam":"Nu"));
//    }
//    public static void main(String[] arg){
//        Main ht = new Main();
//        try{
//            ht.nhap();
//        }
//        catch(IOException e){
//            System.out.println("Da say ra loi nhap xuat : " + e.getMessage());
//        }
//        ht.hien();
//
//    }
//}


// ### nhap ten doi tuong sau do in ra file
//import java.io.*;
//
//public class Main{
//    private String name;
//    private String birdDay;
//    private Boolean gender;
//    public void enterValue() throws IOException{
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        System.out.print("Enter name : ");
//            name = br.readLine();
//        System.out.print("Enter bird day : ");
//            birdDay = br.readLine();
//        System.out.print("Enter gender : ");
//        int g ;
//        try{
//            g = Integer.parseInt(br.readLine());
//            gender = (g == 1?true:false);
//        }
//        catch(NumberFormatException e){
//            System.out.print("Enter 1 or 2 please !");
//            gender = null;
//        }
//    }
//    public void outputFile() throws Exception{
//        PrintStream ps = new PrintStream(new FileOutputStream("HocSinh.txt"));
//        ps.println("Ho va ten : " + name);
//        ps.println("Sinh nam : " + birdDay);
//        ps.println("Gioi tinh : " + (gender == true?"Nam":"Nu"));
//    }
//    public static void main(String[] arg) throws Exception {
//        Main p = new Main();
//        try{
//            p.enterValue();
//        }
//        catch(IOException e){
//            System.out.println("Error : " + e.getMessage());
//        }
//        p.outputFile();
////
////    }
////}
//









