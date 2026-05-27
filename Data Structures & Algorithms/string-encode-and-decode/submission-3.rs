impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut encoded = String::new();

        for s in strs {
            encoded.push_str(&s.len().to_string());
            encoded.push('#');
            encoded.push_str(&s);
        }

        encoded
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut result = Vec::new();
        let bytes = s.as_bytes();
        let mut i = 0;

        while i < s.len() {
            let mut j = i;

            while bytes[j] != b'#' {
                j += 1;
            }

            let length: usize = s[i..j].parse().unwrap();

            i = j + 1;

            let word = s[i..i + length].to_string();
            result.push(word);

            i += length;
        }

        result
    }
}