import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def read_data_from_csv(filename):

    try:
        df = pd.read_csv(filename)

        years = df['Year'].values
        ukraine_data = df['Ukraine'].values
        estonia_data = df['Estonia'].values

        countries_data = {
            'Україна': ukraine_data,
            'Естонія': estonia_data,
            'ukraine': ukraine_data,
            'estonia': estonia_data,
            'ukr': ukraine_data,
            'est': estonia_data
        }

        return years, countries_data, ukraine_data, estonia_data

    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено!")
        return None, None, None, None
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None, None, None, None


def plot_bar_chart_for_country(years, country_data, country_name):

    if years is None or country_data is None:
        print("Немає даних для побудови діаграми!")
        return

    fig, ax = plt.subplots(figsize=(14, 7))

    x = np.arange(len(years))

    color = 'purple' if country_name.lower() in ['україна', 'ukraine', 'ukr'] else 'orange'

    bars = ax.bar(x, country_data,
                  label=country_name,
                  color=color,
                  alpha=0.8,
                  edgecolor='black',
                  linewidth=1)

    ax.set_xlabel('Рік', fontsize=12, color='red', fontweight='bold')
    ax.set_ylabel('Народжуваність на 1000 жінок віком 15-19 років',
                  fontsize=12, color='red', fontweight='bold')
    ax.set_title(f'Рівень народжуваності підлітків у {country_name}\n(пологів на 1000 жінок віком 15-19 років)',
                 fontsize=14, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=45, ha='right')

    ax.legend(fontsize=11)

    ax.grid(True, alpha=0.3, linestyle='--', axis='y')

    for i, bar in enumerate(bars):
        if i % 3 == 0:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=9,
                    fontweight='bold')

    max_value = np.max(country_data)
    max_year = years[np.argmax(country_data)]
    min_value = np.min(country_data)
    min_year = years[np.argmin(country_data)]
    avg_value = np.mean(country_data)

    info_text = f'Максимум: {max_value:.1f} ({max_year})\nМінімум: {min_value:.1f} ({min_year})\nСереднє: {avg_value:.1f}'
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.show()


def plot_comparison_bar_chart(years, ukraine_data, estonia_data):

    if years is None or ukraine_data is None or estonia_data is None:
        print("Немає даних для побудови діаграми!")
        return

    fig, ax = plt.subplots(figsize=(14, 7))

    x = np.arange(len(years))
    width = 0.35

    bars1 = ax.bar(x - width / 2, ukraine_data, width,
                   label='Україна', color='purple', alpha=0.8, edgecolor='black')
    bars2 = ax.bar(x + width / 2, estonia_data, width,
                   label='Естонія', color='orange', alpha=0.8, edgecolor='black')

    ax.set_xlabel('Рік', fontsize=12, color='red', fontweight='bold')
    ax.set_ylabel('Народжуваність на 1000 жінок віком 15-19 років',
                  fontsize=12, color='red', fontweight='bold')
    ax.set_title('Порівняння рівня народжуваності серед підлітків\n(пологів на 1000 жінок віком 15-19 років)',
                 fontsize=14, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=45, ha='right')

    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, linestyle='--', axis='y')

    for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
        if i % 3 == 0:
            ax.text(bar1.get_x() + bar1.get_width() / 2, bar1.get_height() + 0.5,
                    f'{bar1.get_height():.1f}', ha='center', va='bottom', fontsize=8)
            ax.text(bar2.get_x() + bar2.get_width() / 2, bar2.get_height() + 0.5,
                    f'{bar2.get_height():.1f}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()


def plot_line_chart(years, ukraine_data, estonia_data):

    if years is None or ukraine_data is None or estonia_data is None:
        print("Немає даних для побудови графіка!")
        return

    plt.figure(figsize=(12, 7))

    plt.plot(years, ukraine_data,
             label='Україна',
             color='purple',
             linewidth=3,
             marker='o',
             markersize=6,
             linestyle='-')

    plt.plot(years, estonia_data,
             label='Естонія',
             color='orange',
             linewidth=3,
             marker='s',
             markersize=6,
             linestyle='-')

    plt.title('Рівень народжуваності підлітків\n(пологів на 1000 жінок віком 15-19 років)',
              fontsize=14,
              fontweight='bold')

    plt.xlabel('Рік',
               fontsize=12,
               color='red',
               fontweight='bold')

    plt.ylabel('Народжуваність на 1000 жінок віком 15-19 років',
               fontsize=12,
               color='red',
               fontweight='bold')

    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(fontsize=11, loc='upper right')
    plt.xticks(years[::2], rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    csv_filename = 'adolescent_fertility_rate.csv'

    years, countries_data, ukraine_data, estonia_data = read_data_from_csv(csv_filename)

    if years is not None:
        print("=" * 60)
        print("СТАТИСТИЧНА ІНФОРМАЦІЯ ПРО ДАНІ")
        print("=" * 60)
        print(f"Період: {years[0]} - {years[-1]} роки")
        print(f"Кількість років: {len(years)}")

        if ukraine_data is not None:
            print(f"\nУкраїна:")
            print(f"  Максимальне значення: {np.max(ukraine_data):.2f} у {years[np.argmax(ukraine_data)]} році")
            print(f"  Мінімальне значення: {np.min(ukraine_data):.2f} у {years[np.argmin(ukraine_data)]} році")
            print(f"  Середнє значення: {np.mean(ukraine_data):.2f}")

        if estonia_data is not None:
            print(f"\nЕстонія:")
            print(f"  Максимальне значення: {np.max(estonia_data):.2f} у {years[np.argmax(estonia_data)]} році")
            print(f"  Мінімальне значення: {np.min(estonia_data):.2f} у {years[np.argmin(estonia_data)]} році")
            print(f"  Середнє значення: {np.mean(estonia_data):.2f}")
        print("=" * 60)

        while True:
            print("\n" + "=" * 60)
            print("ОБЕРІТЬ ТИП ВІЗУАЛІЗАЦІЇ:")
            print("1 - Побудувати стовпчасту діаграму для однієї країни")
            print("2 - Побудувати порівняльну стовпчасту діаграму (обидві країни)")
            print("3 - Лінійний графік для обох країн")
            print("4 - Вийти з програми")
            print("=" * 60)

            choice = input("Ваш вибір (1/2/3/4): ").strip()

            if choice == '1':
                country_input = input("\nВведіть назву країни (Україна/Естонія або Ukraine/Estonia): ").strip().lower()

                if country_input in ['україна', 'ukraine', 'ukr']:
                    plot_bar_chart_for_country(years, ukraine_data, 'Україна')
                elif country_input in ['естонія', 'estonia', 'est']:
                    plot_bar_chart_for_country(years, estonia_data, 'Естонія')
                else:
                    print(f"\nПомилка: Країну '{country_input}' не знайдено!")
                    print("Доступні країни: Україна, Естонія")

            elif choice == '2':
                plot_comparison_bar_chart(years, ukraine_data, estonia_data)

            elif choice == '3':
                plot_line_chart(years, ukraine_data, estonia_data)

            elif choice == '4':
                print("\nДякуємо за використання програми! До побачення!")
                break

            else:
                print("\nНевірний вибір. Спробуйте ще раз!")


if __name__ == "__main__":
    main()