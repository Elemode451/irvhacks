package com.irvhacks;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import io.github.cdimascio.dotenv.Dotenv;

@SpringBootApplication
@RestController
@CrossOrigin(origins = "http://25.63.224.191:3001/")
public class Main {

    protected static OpenAIClient client;
    protected static String message = "No query yet";
    public static void main(String[] args) {
        Dotenv dotenv = Dotenv.load();
        String apiKey = dotenv.get("OPENAI_API_KEY");

        client = OpenAIOkHttpClient.builder()
            .apiKey(apiKey)
            .build(); 

        SpringApplication.run(Main.class, args);
    }

    @RequestMapping("/")
    public String home() {
        return message; 
    }
}



