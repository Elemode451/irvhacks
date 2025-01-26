package com.irvhacks;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.openai.core.JsonValue;
import com.openai.models.ChatCompletion;
import com.openai.models.ChatCompletionCreateParams;
import com.openai.models.ChatCompletionUserMessageParam;
import com.openai.models.ChatModel;

import io.github.cdimascio.dotenv.Dotenv;

@RestController
public class QueryManager {
    public static final String SEARCH_INFO = "You are to embody the role of a MEDICAL search engine." 
     + "You will only provide names in response to the" 
     + "query that is asked, with no other additional information." 
     + "You will provide a list of up to 15 names. JUST names. Seperate each one with the character |. Make sure it's a full name, and no weird artifacts are included."; 
    
    public static final String DOCTOR_NAME = "If you are provided with a singular name, or asked for information on a DOCTOR'S name, just output the exact name back."; 

    private static HttpClient httpClient = HttpClient.newHttpClient();
    
        @PostMapping("/query")
        public Map<String, String> query(@RequestBody String query)
        {
            if (query == null || query.isEmpty()) {
              Main.message = "NO!";
            }
            ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
            .addMessage(ChatCompletionUserMessageParam.builder()
              .role(JsonValue.from("system"))
              .content(QueryManager.SEARCH_INFO)
              .build())
            .addMessage(ChatCompletionUserMessageParam.builder()
              .role(JsonValue.from("system"))
              .content(QueryManager.DOCTOR_NAME)
              .build())
            .addMessage(ChatCompletionUserMessageParam.builder()
              .role(JsonValue.from("user"))
              .content(query)
              .build())
            .model(ChatModel.GPT_4O_2024_11_20)
            .temperature(0.4)
            .build();
    
            ChatCompletion chatCompletion = Main.client.chat().completions().create(params).validate();  
            String result = chatCompletion.choices().get(0).message().content().get();   
            Main.message = result;
    
            return Map.of("result", result); 
        }
    
        private static class Zembra{ 
            private static final String ZEMBRA_URI = "https://api.zembra.io/listing/find?name=";        
    
            public static List<HttpResponse<String>> queryZembra(List<String> doctors) {
                List<HttpResponse<String>> responses = new ArrayList<>();

                try {
                    List<HttpRequest> requests = new ArrayList<>();
                    
                    for(String doctor : doctors) {
                        requests.add(HttpRequest.newBuilder()
                                    .uri(URI.create(ZEMBRA_URI + doctor))
                                    .GET()
                                    .header("Accept", "application/json")
                                    .header("Authorization", "Bearer " + Dotenv.load().get("ZEMBRA_API_KEY"))
                                    .build());
                    }
        

                    for(var request : requests) {
                        responses.add(httpClient.send(request, HttpResponse.BodyHandlers.ofString()));
                    }

                } catch(Exception e) {
                    e.printStackTrace();
                }

                return responses;
        }

        public static Map<String, Map<String, String>> getZembraResponse(List<HttpResponse<String>> responses) {
            if(responses.isEmpty()) {
                return null;
            }

            for(HttpResponse<String> response : responses) {

            }
        }

    }





    


}
