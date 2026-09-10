def calcular_total(precio, cantidad):
	"""Calcula el total de una compra."""
	if precio < 0 or cantidad < 0:
		raise ValueError("El precio y la cantidad no pueden ser negativos.")

	return precio * cantidad


precio = 10
cantidad = 3
resultado = calcular_total(precio, cantidad)
print(f"El total de la compra es: ${resultado}")
