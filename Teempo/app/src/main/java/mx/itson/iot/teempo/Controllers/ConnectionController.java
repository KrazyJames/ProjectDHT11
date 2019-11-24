package mx.itson.iot.teempo.Controllers;

import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.StandardCharsets;

import mx.itson.iot.teempo.Models.MQTTConnection;

public class ConnectionController {

    private MQTTConnection connection;

    public ConnectionController(MQTTConnection connection) {
        this.connection = connection;
    }

    public void connect() {
        try {
            MqttConnectOptions options = new MqttConnectOptions();
            options.setUserName("jaime.escobar.mtz@gmail.com");
            options.setPassword("IoTGuaymas".toCharArray());
            IMqttToken token = this.connection.getClient().connect(options);
            token.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    // We are connected
                    System.out.println("Connected");
                    subscribe("jaime.escobar.mtz@gmail.com/IoT/Teempo/temp");
                    subscribe("jaime.escobar.mtz@gmail.com/IoT/Teempo/hum");
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    // Something went wrong e.g. connection timeout or firewall problems
                    System.out.println("Connection failed");
                }
            });
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    void publish(String payload) {
        byte[] encodedPayload;
        try {
            encodedPayload = payload.getBytes(StandardCharsets.UTF_8);
            MqttMessage message = new MqttMessage(encodedPayload);
            this.connection.getClient().publish(this.connection.getClientTopic(), message);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    private void subscribe(final String topic) {
        int qos = 1;
        try {
            IMqttToken subToken = this.connection.getClient().subscribe(topic, qos);
            subToken.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    System.out.println("Subscribed " + topic);
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    // The subscription could not be performed, maybe the user was not
                    // authorized to subscribe on the specified topic e.g. using wildcards
                    System.out.println("Something went wrong");
                }
            });
        } catch (MqttException e) {
            e.printStackTrace();
        }

    }
}
