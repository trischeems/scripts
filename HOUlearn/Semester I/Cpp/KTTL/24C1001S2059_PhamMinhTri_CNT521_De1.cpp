// ## Ho Ten : Pham Minh Tri
// ## Lop : CNT521
// ## Ma SV : 24c1001s2059
// ## Mon KTTL : IT05
// ## De so : 01


#include <iostream>
#include <string>
using namespace std;

struct TAINGHE {
    string maTaiNghe;
    string tenTaiNghe;
    string nuocSX;
    int donGia;
    int soLuong;
    int thanhTien;
    TAINGHE* next;
};

TAINGHE* taoNode(string ma, string ten, string nuoc, int gia, int soLuong) {
    TAINGHE* node = new TAINGHE();
    node->maTaiNghe = ma;
    node->tenTaiNghe = ten;
    node->nuocSX = nuoc;
    node->donGia = gia;
    node->soLuong = soLuong;
    node->thanhTien = gia * soLuong;
    node->next = nullptr;
    return node;
}

void themTaiNghe(TAINGHE*& head, TAINGHE* nodeMoi) {
    if (head == nullptr) {
        head = nodeMoi;
    }
    else {
        TAINGHE* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = nodeMoi;
    }
}

void nhapDanhSach(TAINGHE*& head) {
    int n;
    cout << "Nhap so luong tai nghe: ";
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        string ma, ten, nuoc;
        int gia;
        int soLuong;

        cout << "\nNhap thong tin tai nghe thu " << i + 1 << ":\n";
        cout << "Ma tai nghe: ";
        getline(cin, ma);
        cout << "Ten tai nghe: ";
        getline(cin, ten);
        cout << "Nuoc san xuat: ";
        getline(cin, nuoc);
        cout << "Don gia: ";
        cin >> gia;
        cout << "So luong: ";
        cin >> soLuong;
        cin.ignore();

        TAINGHE* nodeMoi = taoNode(ma, ten, nuoc, gia, soLuong);
        themTaiNghe(head, nodeMoi);
    }
}

void hienThiDanhSach(TAINGHE* head) {
    if (head == nullptr) {
        cout << "Danh sach rong.\n";
        return;
    }

    TAINGHE* temp = head;
    cout << "\nDanh sach tai nghe:\n";
    while (temp != nullptr) {
        cout << "Ma tai nghe: " << temp->maTaiNghe << "\n";
        cout << "Ten tai nghe: " << temp->tenTaiNghe << "\n";
        cout << "Nuoc san xuat: " << temp->nuocSX << "\n";
        cout << "Don gia: " << temp->donGia << "\n";
        cout << "So luong: " << temp->soLuong << "\n";
        cout << "Thanh tien: " << temp->thanhTien << "\n\n";
        temp = temp->next;
    }
}

void timKiemTAINGHE(TAINGHE* head, const string& ten) {
    bool found = false;
    TAINGHE* temp = head;
    while (temp != nullptr) {
        if (temp->tenTaiNghe == ten) {
            found = true;
            cout << "Tim thay tai nghe:\n";
            cout << "Ma tai nghe: " << temp->maTaiNghe << "\n";
            cout << "Ten tai nghe: " << temp->tenTaiNghe << "\n";
            cout << "Nuoc san xuat: " << temp->nuocSX << "\n";
            cout << "Don gia: " << temp->donGia << "\n";
            cout << "So luong: " << temp->soLuong << "\n";
            cout << "Thanh tien: " << temp->thanhTien << "\n";
        }
        temp = temp->next;
    }
    if (!found) {
        cout << "Khong tim thay tai nghe co ten la \"" << ten << "\"\n";
    }
}

void sapXepTheoDonGia(TAINGHE*& head) {
    if (head == nullptr || head->next == nullptr) return;

    for (TAINGHE* i = head; i != nullptr; i = i->next) {
        for (TAINGHE* j = i->next; j != nullptr; j = j->next) {
            if (i->donGia > j->donGia) {
                swap(i->maTaiNghe, j->maTaiNghe);
                swap(i->tenTaiNghe, j->tenTaiNghe);
                swap(i->nuocSX, j->nuocSX);
                swap(i->donGia, j->donGia);
                swap(i->soLuong, j->soLuong);
                swap(i->thanhTien, j->thanhTien);
            }
        }
    }
}

int tinhTongTien(TAINGHE* head) {
    int tongTien = 0;
    TAINGHE* temp = head;
    while (temp != nullptr) {
        tongTien += temp->thanhTien;
        temp = temp->next;
    }
    return tongTien;
}

void hienThiDonGiaLonHon250(TAINGHE* head) {
    TAINGHE* temp = head;
    cout << "\nTai nghe co don gia > 250.000:\n";
    while (temp != nullptr) {
        if (temp->donGia > 250000) {
            cout << temp->tenTaiNghe << "\n";
        }
        temp = temp->next;
    }
}

void TAINGHEDonGiaCaoNhat(TAINGHE* head) {
    if (head == nullptr) {
        cout << "Danh sach rong.\n";
        return;
    }

    TAINGHE* maxNode = head;
    TAINGHE* temp = head->next;
    while (temp != nullptr) {
        if (temp->donGia > maxNode->donGia) {
            maxNode = temp;
        }
        temp = temp->next;
    }

    cout << "\nTai nghe co don gia cao nhat:\n";
    cout << "Ma tai nghe: " << maxNode->maTaiNghe << "\n";
    cout << "Ten tai nghe: " << maxNode->tenTaiNghe << "\n";
    cout << "Nuoc san xuat: " << maxNode->nuocSX << "\n";
    cout << "Don gia: " << maxNode->donGia << "\n";
    cout << "So luong: " << maxNode->soLuong << "\n";
    cout << "Thanh tien: " << maxNode->thanhTien << "\n";
}

void giaiPhongDanhSach(TAINGHE*& head) {
    while (head != nullptr) {
        TAINGHE* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    TAINGHE* danhSachTAINGHE = nullptr;

    nhapDanhSach(danhSachTAINGHE);

    hienThiDanhSach(danhSachTAINGHE);

    string tenTimKiem;
    cout << "\nNhap ten tai nghe can tim: ";
    getline(cin, tenTimKiem);
    timKiemTAINGHE(danhSachTAINGHE, tenTimKiem);

    sapXepTheoDonGia(danhSachTAINGHE);
    cout << "\nDanh sach sau khi sap xep theo don gia tang dan:\n";
    hienThiDanhSach(danhSachTAINGHE);

    int tongTien = tinhTongTien(danhSachTAINGHE);
    cout << "\nTong tien cua cac tai nghe: " << tongTien << " VND\n";

    hienThiDonGiaLonHon250(danhSachTAINGHE);

    TAINGHEDonGiaCaoNhat(danhSachTAINGHE);

    giaiPhongDanhSach(danhSachTAINGHE);

    return 0;
}
