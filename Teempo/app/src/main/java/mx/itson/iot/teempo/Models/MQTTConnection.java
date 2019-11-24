package mx.itson.iot.teempo.Models;

import org.eclipse.paho.android.service.MqttAndroidClient;

public class MQTTConnection {
    private String broker;
    private String clientId;
    private MqttAndroidClient client;
    private String clientTopic;

    public MQTTConnection(String broker, String clientId, MqttAndroidClient client, String clientTopic) {
        this.setBroker(broker);
        this.setClientId(clientId);
        this.setClient(client);
        this.setClientTopic(clientTopic);
    }

    public String getBroker() {
        return broker;
    }

    private void setBroker(String broker) {
        this.broker = broker;
    }

    public String getClientId() {
        return clientId;
    }

    private void setClientId(String clientId) {
        this.clientId = clientId;
    }

    public MqttAndroidClient getClient() {
        return client;
    }

    private void setClient(MqttAndroidClient client) {
        this.client = client;
    }

    public String getClientTopic() {
        return clientTopic;
    }

    private void setClientTopic(String clientTopic) {
        this.clientTopic = clientTopic;
    }
}
