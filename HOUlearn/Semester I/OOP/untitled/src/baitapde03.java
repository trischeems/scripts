//import java.io.*;
//import java.util.ArrayList;
//import java.util.Scanner;
//
//class CUDAN {
//    protected String soPhong;
//    protected String tenCD;
//    protected String soDT;
//
//    public CUDAN() {}
//
//    public CUDAN(String soPhong, String tenCD, String soDT) {
//        this.soPhong = soPhong;
//        this.tenCD = tenCD;
//        this.soDT = soDT;
//    }
//
//    public void nhap() {
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap so phong: ");
//        soPhong = sc.nextLine();
//        System.out.print("Nhap ten cu dan: ");
//        tenCD = sc.nextLine();
//        System.out.print("Nhap so dien thoai: ");
//        soDT = sc.nextLine();
//    }
//
//    public void xuat(PrintWriter writer) {
//        writer.printf("So phong: %s\nTen cu dan: %s\nSo dien thoai: %s\n", soPhong, tenCD, soDT);
//    }
//}
//
//class HOADONDICHVU extends CUDAN {
//    private String tenDV;
//    private int soLuongSuDung;
//    private double donGia;
//
//    public HOADONDICHVU() {}
//
//    public HOADONDICHVU(String soPhong, String tenCD, String soDT, String tenDV, int soLuongSuDung, double donGia) {
//        super(soPhong, tenCD, soDT);
//        this.tenDV = tenDV;
//        this.soLuongSuDung = soLuongSuDung;
//        this.donGia = donGia;
//    }
//
//    public void nhap() {
//        super.nhap();
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap loai dich vu: ");
//        tenDV = sc.nextLine();
//        System.out.print("Nhap vao so luong su dung: ");
//        soLuongSuDung = Integer.parseInt(sc.nextLine());
//        System.out.print("Nhap vao so tien don gia: ");
//        donGia = Double.parseDouble(sc.nextLine());
//    }
//
//    public void xuat(PrintWriter writer) {
//        super.xuat(writer);
//        writer.printf("Ten dich vu: %s\nSo luong su dung: %d\nDon gia: %.2f\n", tenDV, soLuongSuDung, donGia);
//    }
//
//    public double thanhTien() {
//        return soLuongSuDung * donGia;
//    }
//}
//
//class Main {
//    private ArrayList<HOADONDICHVU> danhsachcudan = new ArrayList<>();
//
//    public void nhapDanhSach() {
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap so luong cu dan: ");
//        int soLuong = Integer.parseInt(sc.nextLine());
//        for (int i = 0; i < soLuong; i++) {
//            System.out.println("Nhap thong tin cu dan: " + (i + 1));
//            HOADONDICHVU hoadon = new HOADONDICHVU();
//            hoadon.nhap();
//            danhsachcudan.add(hoadon);
//        }
//    }
//    public void xuatDanhSach() {
//        System.out.println("\nDanh sach cu dan:");
//        for (HOADONDICHVU hoadon : danhsachcudan) {
//            hoadon.xuat(new PrintWriter(System.out, true));
//        }
//    }
//
//    public void saveDanhSachVaoFile(String nameFile) throws IOException {
//        try (PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter(nameFile)))) {
//            for (HOADONDICHVU hoadon : danhsachcudan) {
//                hoadon.xuat(writer);
//            }
//        }
//    }
//
//    public double tinhTongDonGia() {
//        double tongtien = 0;
//        for (HOADONDICHVU hoadon : danhsachcudan) {
//            tongtien += hoadon.thanhTien();
//        }
//        return tongtien;
//    }
//
//    public static void main(String[] args) {
//        Main cd = new Main();
//        cd.nhapDanhSach();cd.xuatDanhSach();
//        System.out.printf("\nTong tien hoa don su dung dich vu: %.2f\n", cd.tinhTongDonGia());
//        try {
//            cd.saveDanhSachVaoFile("hoadondichvu.dat");
//        } catch (IOException e) {
//            System.out.println("Loi: " + e.getMessage());
//        }
//    }
//}
