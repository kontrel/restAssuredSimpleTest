package demo;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

public class ApiTest {

//    private static final String ELASTIC_URL = "https://localhost:9200/api-tests/_doc";
//    private static final String ELASTIC_USER = "elastic";
//    private static final String ELASTIC_PASS = "MR8Ydpr+vWHN9pccrE23"; // <- Twoje hasło do Elasticsearch

    @Test
    void shouldReturnCorrectStatusCode() {
        String testName = "GET /users/2";
        String apiUrl = "https://reqres.in/api/users/2";

        Response response = RestAssured.get(apiUrl);
        int statusCode = response.getStatusCode();

        boolean passed = statusCode == 200;

        // Walidacja przykładowa
        assertThat(statusCode, equalTo(200));

//        // Tworzymy wynik testu jako JSON
//        Map<String, Object> testResult = new HashMap<>();
//        testResult.put("testName", testName);
//        testResult.put("timestamp", LocalDateTime.now().toString());
//        testResult.put("apiUrl", apiUrl);
//        testResult.put("statusCode", statusCode);
//        testResult.put("passed", passed);
//        testResult.put("responseTimeMs", response.getTime());

//        // Wysłanie JSON-a do Elasticsearch
//        try {
//            io.restassured.RestAssured
//                    .given()
//                    .auth()
//                    .preemptive()
//                    .basic(ELASTIC_USER, ELASTIC_PASS)
//                    .header("Content-Type", "application/json")
//                    .body(testResult)
//                    .relaxedHTTPSValidation()
//                    .post(ELASTIC_URL)
//                    .then()
//                    .statusCode(201);
//            System.out.println("✅ Test result sent to Elasticsearch successfully!");
//        } catch (Exception e) {
//            System.err.println("❌ Failed to send result to Elasticsearch: " + e.getMessage());
//        }>
    }
}
