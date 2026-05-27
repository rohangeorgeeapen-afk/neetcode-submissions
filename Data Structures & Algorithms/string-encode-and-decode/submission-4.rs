impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        strs.into_iter()
        .map(|w| format!("{}#{}", w.len(), w))
        .collect()
}

    pub fn decode(s: String) -> Vec<String> {
        let mut res = Vec::new();
        let bytes = s.as_bytes();
        let mut i = 0;

        while i < bytes.len() {
            let mut j = i;

            while bytes[j] != b'#' {
                j += 1;
            }

            let length: usize = std::str::from_utf8(&bytes[i..j])
                .unwrap()
                .parse()
                .unwrap();

            let start = j + 1;
            let end = start + length;

            res.push(String::from_utf8(bytes[start..end].to_vec()).unwrap());

            i = end;
        }

        res
    }
}
