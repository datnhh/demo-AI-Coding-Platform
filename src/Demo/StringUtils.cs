namespace Demo;

/// <summary>
/// Vài phép biến đổi chuỗi đơn giản.
/// </summary>
/// <remarks>
/// Cố ý để trống chỗ cho việc mở rộng: repo này tồn tại để agent có thứ gì đó thật để sửa.
/// </remarks>
public static class StringUtils
{
    /// <summary>Đảo ngược một chuỗi.</summary>
    public static string Reverse(string value)
    {
        ArgumentNullException.ThrowIfNull(value);

        char[] characters = value.ToCharArray();
        Array.Reverse(characters);

        return new string(characters);
    }

    /// <summary>Kiểm tra một chuỗi có đối xứng hay không, bỏ qua hoa thường và khoảng trắng.</summary>
    public static bool IsPalindrome(string value)
    {
        ArgumentNullException.ThrowIfNull(value);

        string normalized = new string(value.Where(c => !char.IsWhiteSpace(c)).ToArray()).ToLowerInvariant();
        char[] reversed = normalized.ToCharArray();
        Array.Reverse(reversed);

        return normalized == new string(reversed);
    }

    /// <summary>Chuyển tiếng Việt có dấu về không dấu.</summary>
    public static string RemoveDiacritics(string value)
    {
        ArgumentNullException.ThrowIfNull(value);

        if (string.IsNullOrEmpty(value))
        {
            return value;
        }

        string normalizedString = value.Normalize(System.Text.NormalizationForm.FormD);
        var stringBuilder = new System.Text.StringBuilder(normalizedString.Length);

        foreach (char c in normalizedString)
        {
            var unicodeCategory = System.Globalization.CharUnicodeInfo.GetUnicodeCategory(c);
            if (unicodeCategory != System.Globalization.UnicodeCategory.NonSpacingMark)
            {
                if (c is 'đ')
                {
                    stringBuilder.Append('d');
                }
                else if (c is 'Đ')
                {
                    stringBuilder.Append('D');
                }
                else
                {
                    stringBuilder.Append(c);
                }
            }
        }

        return stringBuilder.ToString().Normalize(System.Text.NormalizationForm.FormC);
    }
}
