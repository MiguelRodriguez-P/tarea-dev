from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    # Implementa acá tu solución
    
    # Caso base: Si el panel no cabe en ninguna orientación, retornamos 0
    panel_vertical = (panel_width <= roof_width and panel_height <= roof_height)
    panel_rotado = (panel_height <= roof_width and panel_width <= roof_height)
    
    if not panel_vertical and not panel_rotado:
        return 0

    # primera opcion: intentar llenar una columna
    width_restante = 0
    if panel_width <= roof_width and panel_height <= roof_height:
        # cuantos caben en la primera columna
        paneles_en_columna = roof_height // panel_height
        # Sumamos mas lo que quepa en el resto del techo
        width_restante = paneles_en_columna + calculate_panels(panel_width, panel_height, 
                                                      roof_width - panel_width, roof_height)

    # OPCIÓN B: Intentar llenar una columna con el panel ROTADO
    height_restante = 0
    if panel_height <= roof_width and panel_width <= roof_height:
        # cuantos caben en la primera columna si rotamos el panel
        paneles_en_columna_r = roof_height // panel_width
        # Sumamos mas lo que quepa en el resto del techo
        height_restante = paneles_en_columna_r + calculate_panels(panel_width, panel_height, 
                                                        roof_width - panel_height, roof_height)

    # retornamos el máximo
    return max(width_restante, height_restante)


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
