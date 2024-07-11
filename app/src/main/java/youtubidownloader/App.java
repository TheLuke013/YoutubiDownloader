package youtubidownloader;

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class App {
    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Hello World GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 100);

        JTextField textField = new JTextField("Hello World");
        textField.setEditable(false);

        frame.getContentPane().add(textField);

        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}
