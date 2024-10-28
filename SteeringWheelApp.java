import javax.swing.*;
import java.awt.*;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;
import javax.sound.sampled.*;

import java.io.File;
import java.io.IOException;

public class SteeringWheelApp {
    private static JLabel statusLabel = new JLabel("Durum: Normal");
    private static JFrame frame = new JFrame("Akıllı Direksiyon Simidi");

    public static void main(String[] args) {
        // Ana pencereyi oluştur
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);

        // Görseli yükle
        ImageIcon steeringWheelImage = new ImageIcon("direksiyon.png");
        JLabel label = new JLabel(steeringWheelImage);
        label.setPreferredSize(new Dimension(300, 300));

        // Durum etiketini ayarla
        statusLabel.setHorizontalAlignment(SwingConstants.CENTER);
        frame.getContentPane().add(statusLabel, BorderLayout.SOUTH);
        frame.getContentPane().add(label, BorderLayout.CENTER);

        frame.pack();
        frame.setVisible(true);

        // Sensör verilerini düzenli olarak güncelle
        startSensorSimulation();
    }

    // Sensör verilerini simüle eden işlev
    private static void startSensorSimulation() {
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                boolean handsOnWheel = isHandsOnWheel(); // Eller direksiyonda mı?
                boolean driverAlert = isDriverAlert();   // Sürücü dikkatli mi?

                if (!handsOnWheel) {
                    showAlert("Eller direksiyonda değil!", Color.RED);
                    playSound();
                } else if (!driverAlert) {
                    showAlert("Dikkat dağınıklığı algılandı!", Color.ORANGE);
                    playSound();
                } else {
                    resetAlert();
                }
            }
        }, 0, 2000); // 2 saniyede bir simülasyon güncelleme
    }

    // Eller direksiyonda mı kontrol eden simülasyon
    private static boolean isHandsOnWheel() {
        Random random = new Random();
        return random.nextBoolean(); // Rastgele true/false döndür
    }

    // Sürücü dikkati kontrol eden simülasyon
    private static boolean isDriverAlert() {
        Random random = new Random();
        return random.nextInt(100) > 20; // %80 ihtimalle dikkatli
    }

    // Uyarı gösteren işlev
    private static void showAlert(String message, Color color) {
        statusLabel.setText("Durum: " + message);
        statusLabel.setForeground(color);
    }

    // Uyarıyı sıfırlayan işlev
    private static void resetAlert() {
        statusLabel.setText("Durum: Normal");
        statusLabel.setForeground(Color.BLACK);
    }

    // Sesli uyarı oynatma işlevi
    private static void playSound() {
        try {
            File soundFile = new File("alert.wav"); // Ses dosyasının yolunu belirt
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(soundFile);
            Clip clip = AudioSystem.getClip();
            clip.open(audioStream);
            clip.start(); // Sesi çal
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
            System.out.println("Ses dosyası çalınamadı: " + e.getMessage());
        }
    }
}
