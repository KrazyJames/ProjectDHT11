package mx.itson.iot.teempo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import mx.itson.iot.teempo.Controllers.ConnectionController;
import mx.itson.iot.teempo.Controllers.DHT11Controller;
import mx.itson.iot.teempo.Models.MQTTConnection;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btnActualizarTemp = findViewById(R.id.btnUpdateTemp);
        Button btnActualizarHum = findViewById(R.id.btnUpdateHum);

        String broker = "tcp://maqiatto.com:1883";
        final String clientTopic = "jaime.escobar.mtz@gmail.com/IoT/Teempo/client";
        final String clientId = MqttClient.generateClientId();
        final MqttAndroidClient client = new MqttAndroidClient(getApplicationContext(), broker, clientId);

        MQTTConnection mqttConnection = new MQTTConnection(broker, clientId, client, clientTopic);
        final ConnectionController connectionController = new ConnectionController(mqttConnection);

        connectionController.connect();
        Toast.makeText(getApplicationContext(), "Connected", Toast.LENGTH_SHORT).show();

        client.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {
                Toast.makeText(getApplicationContext(), "Connection Lost", Toast.LENGTH_LONG).show();
            }

            @Override
            public void messageArrived(String topic, MqttMessage message) {
                String m = new String(message.getPayload());
                if (topic.endsWith("temp")) {
                    String temp = Math.round(Float.parseFloat(m)) + "°C";
                    System.out.println("Temperature: "+temp);
                    TextView txtTemp = findViewById(R.id.txtTemp);
                    txtTemp.setText(temp);
                } else {
                    String hum = Math.round(Float.parseFloat(m)) + "%";
                    System.out.println("Humidity: "+hum);
                    TextView txtHum = findViewById(R.id.txtHum);
                    txtHum.setText(hum);
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });

        final DHT11Controller dht11Controller = new DHT11Controller();
        btnActualizarTemp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dht11Controller.getTemperature(connectionController);
            }
        });
        btnActualizarHum.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dht11Controller.getHumidity(connectionController);
            }
        });
    }

    private void updateFields(){

    }

}

