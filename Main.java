import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("Program başlatılıyor...");
        JFrame frame = new JFrame("Direksiyon Simidi");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        
        // Panel oluşturma
        JPanel panel = new JPanel();
        frame.add(panel);
        placeComponents(panel);
        
        // Pencereyi görünür hale getirme
        frame.setVisible(true);
        
    }

    private static void placeComponents(JPanel panel) {
        panel.setLayout(null);
        
        // Label
        JLabel userLabel = new JLabel("Nabız:");
        userLabel.setBounds(10, 20, 80, 25);
        panel.add(userLabel);
        
        // Text Field
        JTextField userText = new JTextField(20);
        userText.setBounds(100, 20, 165, 25);
        panel.add(userText);
        
        // Button
        JButton loginButton = new JButton("Veri Al");
        loginButton.setBounds(10, 80, 150, 25);
        panel.add(loginButton);
        
        // Örnek görsel veya geri bildirim
        JLabel feedbackLabel = new JLabel("Durum: Normal");
        feedbackLabel.setBounds(10, 120, 300, 25);
        panel.add(feedbackLabel);
    }
}
