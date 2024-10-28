import javax.swing.*;
import java.awt.*;

public class SteeringWheelInterface extends JPanel {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Akıllı Direksiyon Simidi Arayüzü");
        SteeringWheelInterface steeringWheel = new SteeringWheelInterface();
        frame.add(steeringWheel);
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawSteeringWheel(g);
    }

    private void drawSteeringWheel(Graphics g) {
        // Direksiyon simidinin boyutları
        int diameter = 300; // Direksiyon çapı
        int x = (getWidth() - diameter) / 2; // Yatay konum
        int y = (getHeight() - diameter) / 2; // Dikey konum
        
        // Direksiyon simidini çizme
        g.setColor(Color.GRAY);
        g.fillOval(x, y, diameter, diameter); // Dış daire

        // İç daire (kavrama yeri)
        g.setColor(Color.BLACK);
        g.fillOval(x + 30, y + 30, diameter - 60, diameter - 60); // İç daire

        // Direksiyon simidi üzerindeki merkezi nokta
        g.setColor(Color.RED);
        g.fillOval(x + diameter / 2 - 5, y + diameter / 2 - 5, 10, 10); // Merkez nokta

        // Dış kenara çizgi ekleme
        g.setColor(Color.DARK_GRAY);
        g.drawOval(x, y, diameter, diameter); // Dış çerçeve
    }
}
