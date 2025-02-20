// Superclase Pieza
public abstract class Pieza {
    protected boolean esBlanca;

    public Pieza(boolean esBlanca) {
        this.esBlanca = esBlanca;
    }

    public boolean esBlanca() {
        return esBlanca;
    }

    // Método abstracto para mover
    public abstract boolean mover(int filaInicial, int colInicial, int filaFinal, int colFinal, Pieza[][] tablero);

    // Método para capturar (comer) una pieza
    public boolean comer(Pieza objetivo) {
        if (objetivo != null && objetivo.esBlanca() != this.esBlanca) {
            return true; // Se puede comer
        }
        return false;
    }

    // Método cuando una pieza es capturada
    public void serComido() {
        System.out.println("Esta pieza ha sido comida.");
    }
}

// Subclase Rey
class Rey extends Pieza {
    public Rey(boolean esBlanca) {
        super(esBlanca);
    }

    @Override
    public boolean mover(int filaInicial, int colInicial, int filaFinal, int colFinal, Pieza[][] tablero) {
        // El rey solo se mueve una casilla en cualquier dirección
        int filaMov = Math.abs(filaFinal - filaInicial);
        int colMov = Math.abs(colFinal - colInicial);
        return (filaMov <= 1 && colMov <= 1);
    }

    @Override
    public String toString() {
        return esBlanca ? "♔" : "♚";
    }
}

// Subclase Torre
class Torre extends Pieza {
    public Torre(boolean esBlanca) {
        super(esBlanca);
    }

    @Override
    public boolean mover(int filaInicial, int colInicial, int filaFinal, int colFinal, Pieza[][] tablero) {
        // La torre se mueve en línea recta (horizontal o vertical)
        return (filaInicial == filaFinal || colInicial == colFinal);
    }

    @Override
    public String toString() {
        return esBlanca ? "♖" : "♜";
    }
}

// Clase Tablero
class Tablero {
    private Pieza[][] tablero;

    public Tablero() {
        tablero = new Pieza[8][8];
        inicializarTablero();
    }

    private void inicializarTablero() {
        // Inicializar las piezas en las posiciones iniciales
        tablero[0][0] = new Torre(false); // Torre negra
        tablero[0][7] = new Torre(false); // Torre negra
        tablero[7][0] = new Torre(true);  // Torre blanca
        tablero[7][7] = new Torre(true);  // Torre blanca

        tablero[0][4] = new Rey(false);   // Rey negro
        tablero[7][4] = new Rey(true);    // Rey blanco

        // Otras piezas pueden ser inicializadas aquí
    }

    public void imprimirTablero() {
        for (int fila = 0; fila < 8; fila++) {
            for (int col = 0; col < 8; col++) {
                if (tablero[fila][col] != null) {
                    System.out.print(tablero[fila][col] + " ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

    public boolean moverPieza(int filaInicial, int colInicial, int filaFinal, int colFinal) {
        Pieza pieza = tablero[filaInicial][colInicial];
        if (pieza != null && pieza.mover(filaInicial, colInicial, filaFinal, colFinal, tablero)) {
            Pieza objetivo = tablero[filaFinal][colFinal];
            if (objetivo != null && pieza.comer(objetivo)) {
                objetivo.serComido();
            }
            tablero[filaFinal][colFinal] = pieza;
            tablero[filaInicial][colInicial] = null;
            return true;
        }
        return false;
    }
}

// Programa principal
public class Ajedrez {
    public static void main(String[] args) {
        Tablero tablero = new Tablero();
        tablero.imprimirTablero();
        
        System.out.println("Moviendo la torre...");
        tablero.moverPieza(7, 0, 5, 0); // Mover la torre blanca
        tablero.imprimirTablero();
    }
}
