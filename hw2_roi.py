def main():
    print("=== TÍNH TỶ SUẤT SINH LỜI TRÊN VỐN ĐẦU TƯ (ROI) ===")
    
    try:
        # Nhập dữ liệu đầu vào từ bàn phím
        initial_investment = float(input("Nhập tổng vốn ban đầu (đồng): "))
        final_value = float(input("Nhập tổng giá trị bán ra (đồng): "))
        
        # 1. Tính lợi nhuận ròng (Net Profit)
        net_profit = final_value - initial_investment
        
        # 2. Tính tỷ lệ ROI (%)
        if initial_investment == 0:
            print("❌ Vốn ban đầu phải lớn hơn 0 để tính ROI!")
            return
            
        roi = (net_profit / initial_investment) * 100
        
        # 3. In kết quả ra màn hình (làm tròn ROI đến 2 chữ số thập phân)
        print("\n--- KẾT QUẢ ĐẦU TƯ ---")
        print(f"Tổng vốn ban đầu : {initial_investment:,.0f} đồng")
        print(f"Giá trị thu về   : {final_value:,.0f} đồng")
        print(f"Lợi nhuận ròng   : {net_profit:,.0f} đồng")
        print(f"👉 Tỷ suất ROI   : {roi:.2f}%")
        
    except ValueError:
        print("❌ Vui lòng chỉ nhập số hợp lệ!")

if __name__ == "__main__":
    main()
